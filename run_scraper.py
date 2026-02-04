"""
Quick start example for Google Maps Scraper
"""

import asyncio
from scraper_simple import GoogleMapsScraper


async def main():
    """
    Simple example: Scrape plumbers and electricians
    """
    print("\n" + "="*60)
    print("GOOGLE MAPS SCRAPER - QUICK START")
    print("="*60)

    # Define what to scrape
    queries = [
        "plumbers in New York",
        "electricians in New York",
    ]

    # Create scraper
    scraper = GoogleMapsScraper(output_dir="./output")

    print(f"\n🔍 Scraping {len(queries)} search queries...")
    print("This may take a few minutes...\n")

    # Run scraper
    await scraper.scrape_multiple(queries, max_per_query=15)

    # Filter for businesses WITHOUT websites (your target market)
    no_website = scraper.filter_no_website()

    # Save results
    json_file = scraper.save_results()
    csv_file = scraper.save_csv()

    # Print summary
    scraper.print_summary()

    print(f"\n📊 RESULTS SUMMARY:")
    print(f"Total businesses scraped: {len(scraper.businesses)}")
    print(
        f"Businesses WITHOUT websites: {len(no_website)} ← Perfect for landing pages! 🎯")
    print(f"\n📁 Files saved:")
    print(f"   JSON: {json_file}")
    if csv_file:
        print(f"   CSV: {csv_file}")

    print(f"\n✅ Next steps:")
    print(f"1. Open the CSV file to view and filter results")
    print(f"2. Contact the businesses without websites")
    print(f"3. Build landing pages for them!")


if __name__ == "__main__":
    asyncio.run(main())
