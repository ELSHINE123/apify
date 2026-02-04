"""
Google Maps Business Scraper for Small & Medium Businesses Without Websites
Extracts business data suitable for building landing pages
"""

import asyncio
import json
import logging
from datetime import datetime
from typing import Optional
from pathlib import Path

from crawlee.playwright_crawler import PlaywrightCrawler
from crawlee.configuration import Configuration
from crawlee import CrawlResult


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class GoogleMapsScraper:
    """Scraper for Google Maps businesses without websites"""

    def __init__(self, search_queries: list[str], output_dir: str = "./output"):
        """
        Initialize the scraper.

        Args:
            search_queries: List of search queries (e.g., ["restaurants in New York", "plumbers in Boston"])
            output_dir: Directory to save results
        """
        self.search_queries = search_queries
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.businesses = []
        self.crawler = None

    async def scrape_google_maps(self) -> list[dict]:
        """
        Scrape Google Maps for businesses without websites.

        Returns:
            List of business dictionaries with extracted data
        """
        # Configure Crawlee
        configuration = Configuration(
            persistent_storage_enabled=False,
            max_request_retries=3,
        )

        # Create crawler
        self.crawler = PlaywrightCrawler(
            configuration=configuration,
            max_requests_per_crawl=100,
            max_crawl_depth=2,
        )

        @self.crawler.router.default_handler
        async def handle_page(context):
            """Handle Google Maps search results page"""
            try:
                page = context.page
                await page.wait_for_load_state("networkidle", timeout=10000)

                # Get all business listings
                businesses = await page.locator('[role="feed"] > div').all()
                logger.info(f"Found {len(businesses)} business listings")

                for business_elem in businesses:
                    try:
                        # Extract business information
                        business_data = await self._extract_business_data(business_elem, page)

                        if business_data and not self._has_website(business_data):
                            self.businesses.append(business_data)
                            logger.info(
                                f"Added: {business_data.get('name', 'Unknown')}")

                    except Exception as e:
                        logger.warning(f"Error extracting business data: {e}")
                        continue

            except Exception as e:
                logger.error(f"Error handling page: {e}")

        # Process each search query
        for query in self.search_queries:
            logger.info(f"Scraping: {query}")
            search_url = self._build_google_maps_url(query)

            try:
                await self.crawler.run([search_url])
            except Exception as e:
                logger.error(f"Error scraping {query}: {e}")
                continue

        return self.businesses

    async def _extract_business_data(self, element, page) -> Optional[dict]:
        """Extract business information from listing element"""
        try:
            # Extract business name
            name_elem = await element.locator('h3').first.inner_text()
            if not name_elem:
                return None

            # Extract rating
            rating = None
            try:
                rating_text = await element.locator('[role="img"]').first.get_attribute('aria-label')
                if rating_text and 'star' in rating_text:
                    rating = float(rating_text.split()[0])
            except:
                pass

            # Extract address
            address = None
            try:
                address = await element.locator('span:has-text("Address")').first.inner_text()
            except:
                pass

            # Extract phone
            phone = None
            try:
                phone = await element.locator('span:has-text("Phone")').first.inner_text()
            except:
                pass

            # Extract website (to filter out)
            website = None
            try:
                website = await element.locator('a[href*="http"]').first.get_attribute('href')
            except:
                pass

            # Extract review count
            review_count = None
            try:
                review_text = await element.locator('text=/\\(\\d+\\)').first.inner_text()
                if review_text:
                    review_count = int(review_text.strip('()'))
            except:
                pass

            return {
                'name': name_elem,
                'rating': rating,
                'review_count': review_count,
                'address': address,
                'phone': phone,
                'website': website,
                'scraped_at': datetime.now().isoformat(),
            }

        except Exception as e:
            logger.warning(f"Error extracting business data: {e}")
            return None

    def _has_website(self, business_data: dict) -> bool:
        """Check if business has a website"""
        return bool(business_data.get('website'))

    def _build_google_maps_url(self, query: str) -> str:
        """Build Google Maps search URL"""
        # Note: Direct Google Maps scraping is challenging due to JavaScript rendering
        # This URL pattern works with headless browsers
        query_encoded = query.replace(' ', '+')
        return f"https://www.google.com/maps/search/{query_encoded}"

    def save_results(self, filename: Optional[str] = None) -> str:
        """
        Save scraped businesses to JSON file.

        Args:
            filename: Output filename (default: auto-generated with timestamp)

        Returns:
            Path to saved file
        """
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"google_maps_businesses_{timestamp}.json"

        filepath = self.output_dir / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.businesses, f, indent=2, ensure_ascii=False)

        logger.info(f"Saved {len(self.businesses)} businesses to {filepath}")
        return str(filepath)

    def save_csv(self, filename: Optional[str] = None) -> str:
        """
        Save results to CSV for easier viewing in spreadsheets.

        Args:
            filename: Output filename

        Returns:
            Path to saved file
        """
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
            logger.warning(
                "pandas not installed. Install it to use CSV export.")
            return None

    def print_summary(self):
        """Print summary of scraped businesses"""
        print("\n" + "="*80)
        print(f"SCRAPING SUMMARY - {len(self.businesses)} businesses found")
        print("="*80)

        for i, biz in enumerate(self.businesses, 1):
            print(f"\n{i}. {biz.get('name', 'Unknown')}")
            print(
                f"   Rating: {biz.get('rating', 'N/A')} ⭐ ({biz.get('review_count', 0)} reviews)")
            print(f"   Address: {biz.get('address', 'N/A')}")
            print(f"   Phone: {biz.get('phone', 'N/A')}")

        print("\n" + "="*80)


async def main():
    """Example usage of the scraper"""

    # Define search queries - customize these for your needs
    search_queries = [
        "plumbers in New York",
        "restaurants in Boston",
        "salons in Chicago",
    ]

    # Initialize scraper
    scraper = GoogleMapsScraper(search_queries)

    # Run scraper
    logger.info("Starting Google Maps scraper...")
    businesses = await scraper.scrape_google_maps()

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
