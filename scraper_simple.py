"""
Google Maps Business Scraper - Simplified Version
Extracts business data from Google Maps using Playwright browser automation
Focus: Small & Medium Businesses (SMBs) without websites
"""

import asyncio
import json
import logging
from datetime import datetime
from typing import Optional
from pathlib import Path

from playwright.async_api import async_playwright, Browser, Page


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class GoogleMapsScraper:
    """Scraper for Google Maps businesses"""

    def __init__(self, output_dir: str = "./output"):
        """
        Initialize the scraper.

        Args:
            output_dir: Directory to save results
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.businesses = []

    async def scrape_query(self, query: str, max_results: int = 20) -> list[dict]:
        """
        Scrape Google Maps for a specific search query.

        Args:
            query: Search query (e.g., "plumbers in New York")
            max_results: Maximum number of results to extract

        Returns:
            List of business dictionaries
        """
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()

            try:
                logger.info(f"Scraping: {query}")

                # Build and navigate to Google Maps search
                search_url = self._build_google_maps_url(query)
                await page.goto(search_url, wait_until='networkidle', timeout=30000)

                # Wait for results to load
                await page.wait_for_timeout(3000)

                businesses = await self._extract_businesses(page, max_results)
                self.businesses.extend(businesses)

                logger.info(
                    f"Found {len(businesses)} businesses for '{query}'")
                return businesses

            except Exception as e:
                logger.error(f"Error scraping '{query}': {e}")
                return []

            finally:
                await browser.close()

    async def _extract_businesses(self, page: Page, max_results: int) -> list[dict]:
        """Extract business information from the page"""
        businesses = []

        try:
            # Scroll through results to load more
            for _ in range(3):
                await page.evaluate("window.scrollBy(0, window.innerHeight)")
                await page.wait_for_timeout(1000)

            # Find all business listing elements
            listings = await page.query_selector_all('[data-index]')
            logger.info(f"Found {len(listings)} listing elements")

            for i, listing in enumerate(listings[:max_results]):
                try:
                    # Extract business name
                    name_elem = await listing.query_selector('h3')
                    if not name_elem:
                        continue

                    name = await name_elem.inner_text()
                    if not name:
                        continue

                    # Get the business link/data
                    link_elem = await listing.query_selector('a[href*="maps/place"]')

                    business_data = {
                        'name': name.strip(),
                        'rating': None,
                        'review_count': None,
                        'address': None,
                        'phone': None,
                        'website': None,
                        'scraped_at': datetime.now().isoformat(),
                    }

                    # Try to extract rating
                    try:
                        rating_elem = await listing.query_selector('[role="img"]')
                        if rating_elem:
                            rating_text = await rating_elem.get_attribute('aria-label')
                            if rating_text and 'star' in rating_text.lower():
                                rating_str = rating_text.split()[0]
                                business_data['rating'] = float(rating_str)
                    except:
                        pass

                    # Try to extract review count
                    try:
                        review_elem = await listing.query_selector('text=/\\(\\d+\\)/')
                        if review_elem:
                            review_text = await review_elem.inner_text()
                            review_count = int(review_text.strip('()'))
                            business_data['review_count'] = review_count
                    except:
                        pass

                    # Try to extract address
                    try:
                        addr_elem = await listing.query_selector('text=/^Address/')
                        if addr_elem:
                            parent = await addr_elem.evaluate_handle("el => el.parentElement.parentElement")
                            addr_text = await parent.evaluate("el => el.innerText")
                            business_data['address'] = addr_text.replace(
                                'Address\n', '').strip()
                    except:
                        pass

                    # Try to extract phone
                    try:
                        phone_elem = await listing.query_selector('text=/Phone/')
                        if phone_elem:
                            parent = await phone_elem.evaluate_handle("el => el.parentElement.parentElement")
                            phone_text = await parent.evaluate("el => el.innerText")
                            business_data['phone'] = phone_text.replace(
                                'Phone\n', '').strip()
                    except:
                        pass

                    # Check for website (we want businesses WITHOUT websites)
                    try:
                        website_elem = await listing.query_selector('a[href*="http"]')
                        if website_elem and 'maps' not in await website_elem.get_attribute('href'):
                            website = await website_elem.get_attribute('href')
                            business_data['website'] = website
                    except:
                        pass

                    # Only add if we have a name
                    if business_data['name']:
                        businesses.append(business_data)

                except Exception as e:
                    logger.warning(f"Error extracting business {i}: {e}")
                    continue

            return businesses

        except Exception as e:
            logger.error(f"Error extracting businesses: {e}")
            return businesses

    def _build_google_maps_url(self, query: str) -> str:
        """Build Google Maps search URL"""
        query_encoded = query.replace(' ', '+')
        return f"https://www.google.com/maps/search/{query_encoded}"

    async def scrape_multiple(self, queries: list[str], max_per_query: int = 20):
        """
        Scrape multiple search queries.

        Args:
            queries: List of search queries
            max_per_query: Max results per query
        """
        for query in queries:
            await self.scrape_query(query, max_per_query)
            await asyncio.sleep(2)  # Be respectful with timing

    def filter_no_website(self) -> list[dict]:
        """Filter businesses that don't have a website"""
        return [b for b in self.businesses if not b.get('website')]

    def filter_by_rating(self, min_rating: float = 4.0) -> list[dict]:
        """Filter businesses by minimum rating"""
        return [b for b in self.businesses if (b.get('rating') or 0) >= min_rating]

    def save_results(self, filename: Optional[str] = None) -> str:
        """Save results to JSON"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"google_maps_businesses_{timestamp}.json"

        filepath = self.output_dir / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.businesses, f, indent=2, ensure_ascii=False)

        logger.info(f"Saved {len(self.businesses)} businesses to {filepath}")
        return str(filepath)

    def save_csv(self, filename: Optional[str] = None) -> str:
        """Save results to CSV"""
        try:
            import pandas as pd

            if not filename:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"google_maps_businesses_{timestamp}.csv"

            filepath = self.output_dir / filename
            df = pd.DataFrame(self.businesses)
            df.to_csv(filepath, index=False, encoding='utf-8')

            logger.info(
                f"Saved {len(self.businesses)} businesses to {filepath}")
            return str(filepath)
        except ImportError:
            logger.warning("pandas not installed. Skipping CSV export.")
            return None

    def print_summary(self):
        """Print summary of scraped businesses"""
        no_website = self.filter_no_website()

        print("\n" + "="*80)
        print(f"SCRAPING SUMMARY - {len(self.businesses)} businesses found")
        print(f"Businesses WITHOUT websites: {len(no_website)} ✅")
        print("="*80)

        for i, biz in enumerate(no_website[:10], 1):  # Show first 10
            print(f"\n{i}. {biz.get('name', 'Unknown')}")
            print(
                f"   Rating: {biz.get('rating', 'N/A')} ⭐ ({biz.get('review_count', 0)} reviews)")
            print(f"   Address: {biz.get('address', 'N/A')}")
            print(f"   Phone: {biz.get('phone', 'N/A')}")

        if len(no_website) > 10:
            print(f"\n... and {len(no_website) - 10} more businesses")

        print("\n" + "="*80)


async def main():
    """Example usage"""
    queries = [
        "plumbers in New York",
        "electricians in Los Angeles",
    ]

    scraper = GoogleMapsScraper()

    # Scrape multiple queries
    await scraper.scrape_multiple(queries, max_per_query=20)

    # Save results
    json_file = scraper.save_results()
    csv_file = scraper.save_csv()

    # Print summary
    scraper.print_summary()

    print(f"\n✅ Scraping complete!")
    print(f"📄 Results saved to:")
    print(f"   - JSON: {json_file}")
    if csv_file:
        print(f"   - CSV: {csv_file}")


if __name__ == "__main__":
    asyncio.run(main())
