"""
Example script showing how to use the Google Maps Scraper
"""

import asyncio
from scraper import GoogleMapsScraper


async def example_1_basic_scrape():
    """Example 1: Basic scraping for multiple business types"""
    print("\n📌 Example 1: Basic Scraping")
    print("-" * 50)

    queries = [
        "plumbers in New York",
        "electricians in Los Angeles",
        "personal trainers in Chicago",
    ]

    scraper = GoogleMapsScraper(queries)
    businesses = await scraper.scrape_google_maps()

    scraper.save_results("example1_basic.json")
    scraper.save_csv("example1_basic.csv")
    scraper.print_summary()


async def example_2_specific_location():
    """Example 2: Target specific location and business type"""
    print("\n📌 Example 2: Specific Location Targeting")
    print("-" * 50)

    queries = [
        "auto repair shops in Austin Texas",
        "dental clinics in Denver Colorado",
        "pet grooming in Seattle Washington",
    ]

    scraper = GoogleMapsScraper(queries, output_dir="./output/location_based")
    businesses = await scraper.scrape_google_maps()

    scraper.save_results()
    scraper.save_csv()
    print(f"✅ Found {len(businesses)} businesses without websites")


async def example_3_broad_search():
    """Example 3: Broader search for SMBs in multiple categories"""
    print("\n📌 Example 3: Broad SMB Search")
    print("-" * 50)

    queries = [
        "home cleaning services",
        "carpet cleaning",
        "landscape gardening",
        "handyman services",
        "painting contractors",
        "roofing contractors",
    ]

    scraper = GoogleMapsScraper(queries, output_dir="./output/smb_broad")
    businesses = await scraper.scrape_google_maps()

    scraper.save_results()
    scraper.save_csv()

    # Filter results
    no_website = [b for b in businesses if not b.get('website')]
    print(f"\n✅ Total found: {len(businesses)}")
    print(f"✅ Without websites: {len(no_website)}")


async def run_all_examples():
    """Run all examples"""
    print("\n" + "="*50)
    print("GOOGLE MAPS SCRAPER - USAGE EXAMPLES")
    print("="*50)

    try:
        # Uncomment to run individual examples
        # await example_1_basic_scrape()
        # await example_2_specific_location()
        await example_3_broad_search()

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    asyncio.run(run_all_examples())
