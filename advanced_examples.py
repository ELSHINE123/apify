"""
Advanced usage patterns and integration examples
"""

import asyncio
import json
from scraper import GoogleMapsScraper


async def scrape_and_filter_no_website():
    """Scrape and filter only businesses WITHOUT websites"""
    queries = [
        "plumbers in New York",
        "electricians in New York",
    ]

    scraper = GoogleMapsScraper(queries)
    all_businesses = await scraper.scrape_google_maps()

    # Filter for businesses without websites
    no_website_businesses = [
        b for b in all_businesses
        if not b.get('website')
    ]

    print(f"Total found: {len(all_businesses)}")
    print(f"Without websites: {len(no_website_businesses)}")

    return no_website_businesses


async def scrape_by_rating_and_reviews():
    """Scrape and filter by rating and review count"""
    queries = ["restaurants in San Francisco"]

    scraper = GoogleMapsScraper(queries)
    all_businesses = await scraper.scrape_google_maps()

    # Filter for high-rated, established businesses
    quality_businesses = [
        b for b in all_businesses
        if (b.get('rating', 0) >= 4.0 and
            b.get('review_count', 0) >= 10 and
            not b.get('website'))
    ]

    return quality_businesses


async def scrape_multiple_cities():
    """Scrape same business type across multiple cities"""
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
    business_type = "plumbers"

    all_businesses = []

    for city in cities:
        print(f"\n🔍 Scraping {business_type} in {city}...")
        query = f"{business_type} in {city}"

        scraper = GoogleMapsScraper([query])
        businesses = await scraper.scrape_google_maps()

        # Add city info to each business
        for b in businesses:
            b['city'] = city
            b['business_type'] = business_type

        all_businesses.extend(businesses)

    return all_businesses


async def scrape_and_export_to_database_format():
    """Scrape and format for database/CRM import"""
    queries = ["salons in Los Angeles"]

    scraper = GoogleMapsScraper(queries)
    businesses = await scraper.scrape_google_maps()

    # Transform for database insertion
    db_format = []
    for b in businesses:
        db_format.append({
            'business_name': b.get('name'),
            'phone_number': b.get('phone'),
            'street_address': b.get('address'),
            'website_url': b.get('website'),
            'google_rating': b.get('rating'),
            'review_count': b.get('review_count'),
            'has_website': bool(b.get('website')),
            'needs_landing_page': not bool(b.get('website')),
            'imported_date': b.get('scraped_at'),
        })

    # Save in database-friendly format
    with open('db_import.json', 'w') as f:
        json.dump(db_format, f, indent=2)

    return db_format


async def example_landing_page_lead_generation():
    """
    Comprehensive example: Find SMBs perfect for landing page services
    Focus: Businesses with strong reputation but no online presence
    """
    print("\n" + "="*60)
    print("LEAD GENERATION FOR LANDING PAGE SERVICES")
    print("="*60)

    # Define industries that typically benefit from landing pages
    queries = [
        "plumbers in New York",
        "electricians in New York",
        "hvac contractors in New York",
        "roofing contractors in New York",
        "auto mechanics in New York",
    ]

    scraper = GoogleMapsScraper(
        queries, output_dir="./output/landing_page_leads")
    all_businesses = await scraper.scrape_google_maps()

    # Filter for perfect landing page candidates:
    # - No website (need landing page service)
    # - Good ratings (proven business)
    # - Multiple reviews (established)
    landing_page_candidates = [
        b for b in all_businesses
        if (not b.get('website') and
            b.get('rating', 0) >= 4.0 and
            b.get('review_count', 0) >= 5)
    ]

    print(f"\n📊 RESULTS:")
    print(f"Total businesses found: {len(all_businesses)}")
    print(
        f"Without websites: {len([b for b in all_businesses if not b.get('website')])}")
    print(f"Perfect landing page leads: {len(landing_page_candidates)}")

    # Save results
    scraper.businesses = landing_page_candidates
    scraper.save_results("landing_page_leads.json")
    scraper.save_csv("landing_page_leads.csv")

    print(f"\n✅ Results saved to output/landing_page_leads/")
    print(
        f"\n🎯 These {len(landing_page_candidates)} businesses are perfect candidates for landing pages!")


async def scrape_with_retries():
    """Example with custom retry logic for failed queries"""
    queries = [
        "plumbers in New York",
        "electricians in Los Angeles",
    ]

    all_results = []
    max_retries = 3

    for query in queries:
        for attempt in range(max_retries):
            try:
                print(f"Attempt {attempt + 1}/{max_retries}: {query}")
                scraper = GoogleMapsScraper([query])
                results = await scraper.scrape_google_maps()
                all_results.extend(results)
                break
            except Exception as e:
                print(f"  ❌ Failed: {e}")
                if attempt < max_retries - 1:
                    await asyncio.sleep(2 ** attempt)  # Exponential backoff
                else:
                    print(
                        f"  ⚠️  Skipping {query} after {max_retries} attempts")

    return all_results


if __name__ == "__main__":
    # Run the main landing page lead generation example
    asyncio.run(example_landing_page_lead_generation())

    # Uncomment below to run other examples:
    # asyncio.run(scrape_and_filter_no_website())
    # asyncio.run(scrape_by_rating_and_reviews())
    # asyncio.run(scrape_multiple_cities())
    # asyncio.run(scrape_and_export_to_database_format())
