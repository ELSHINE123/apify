"""
Google Maps Business Scraper - Apify Actor Entry Point
Runs as an Apify Actor on the Apify platform
"""

import asyncio
import json
import logging
from datetime import datetime
from apify import Actor
from scraper_simple import GoogleMapsScraper


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def main():
    """Main entry point for the Apify Actor"""

    async with Actor:
        # Get input from the Apify platform
        actor_input = await Actor.get_input() or {}

        # Extract parameters with defaults
        search_queries = actor_input.get(
            'searchQueries', ['plumbers in New York'])
        max_results = actor_input.get('maxResultsPerQuery', 20)
        filter_no_website = actor_input.get('filterNoWebsite', True)
        min_rating = actor_input.get('minRating')
        min_review_count = actor_input.get('minReviewCount')

        logger.info(f"Starting Google Maps scraper")
        logger.info(f"Queries: {search_queries}")
        logger.info(f"Max results per query: {max_results}")

        # Initialize scraper
        scraper = GoogleMapsScraper()

        # Run scraping
        try:
            await scraper.scrape_multiple(search_queries, max_per_query=max_results)
            logger.info(f"Scraped {len(scraper.businesses)} businesses total")
        except Exception as e:
            logger.error(f"Error during scraping: {e}")
            raise

        # Apply filters
        results = scraper.businesses

        if filter_no_website:
            results = scraper.filter_no_website()
            logger.info(
                f"Filtered to {len(results)} businesses without websites")

        if min_rating:
            results = [b for b in results if (
                b.get('rating') or 0) >= min_rating]
            logger.info(
                f"Filtered to {len(results)} businesses with rating >= {min_rating}")

        if min_review_count:
            results = [b for b in results if (
                b.get('review_count') or 0) >= min_review_count]
            logger.info(
                f"Filtered to {len(results)} businesses with {min_review_count}+ reviews")

        # Push results to Apify dataset
        for business in results:
            await Actor.push_data(business)

        logger.info(f"✅ Pushed {len(results)} businesses to dataset")

        # Store summary in key-value store
        summary = {
            'total_scraped': len(scraper.businesses),
            'total_returned': len(results),
            'queries': search_queries,
            'scraped_at': datetime.now().isoformat(),
        }
        await Actor.set_value('summary', summary)

        logger.info(f"Actor execution completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())
