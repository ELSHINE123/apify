# Google Maps Business Scraper for Landing Page Creation

A Python web scraper built with **Crawlee** that extracts small and medium business (SMB) data from Google Maps, specifically targeting businesses **without websites**. Perfect for building landing pages and lead generation.

## 🎯 Features

- **Target SMBs without websites** - Focus on businesses that need your landing page services
- **Extract key business data** - Name, phone, address, rating, reviews
- **Multiple export formats** - JSON and CSV for easy integration
- **Async crawling** - Fast, efficient scraping with proper error handling
- **Customizable queries** - Search by business type, location, and category
- **Logging & monitoring** - Track progress and debug issues easily

## 📋 Requirements

- Python 3.9+
- Crawlee (async web scraping framework)
- Playwright (for headless browser automation)
- Pandas (optional, for CSV export)

## 🚀 Quick Start

### 1. Installation

```bash
# Clone or navigate to the project directory
cd google-maps-scraper

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### 2. Basic Usage

Edit `examples.py` and uncomment the example you want to run, then:

```bash
python examples.py
```

Or use the scraper directly in your code:

```python
import asyncio
from scraper import GoogleMapsScraper

async def main():
    queries = [
        "plumbers in New York",
        "electricians in Los Angeles",
    ]

    scraper = GoogleMapsScraper(queries)
    businesses = await scraper.scrape_google_maps()

    scraper.save_results()
    scraper.save_csv()
    scraper.print_summary()

asyncio.run(main())
```

## 📊 Output Format

### JSON Output

```json
[
  {
    "name": "John's Plumbing Services",
    "rating": 4.8,
    "review_count": 42,
    "address": "123 Main St, New York, NY 10001",
    "phone": "+1 (212) 555-1234",
    "website": null,
    "scraped_at": "2024-02-04T10:30:45.123456"
  },
  ...
]
```

### CSV Output

Perfect for importing into spreadsheets, databases, or CRM systems.

| name            | rating | review_count | address        | phone | website | scraped_at |
| --------------- | ------ | ------------ | -------------- | ----- | ------- | ---------- |
| John's Plumbing | 4.8    | 42           | 123 Main St... | +1... | null    | ...        |

## 🔍 Usage Examples

### Example 1: Basic Multi-Category Search

```python
queries = [
    "plumbers in New York",
    "electricians in New York",
    "hvac contractors in New York",
]
scraper = GoogleMapsScraper(queries)
```

### Example 2: Geographic Targeting

```python
queries = [
    "auto repair shops in Austin Texas",
    "dental clinics in Denver Colorado",
    "pet grooming in Seattle Washington",
]
scraper = GoogleMapsScraper(queries)
```

### Example 3: Broad SMB Search

```python
queries = [
    "home cleaning services",
    "carpet cleaning",
    "landscape gardening",
    "handyman services",
    "painting contractors",
    "roofing contractors",
]
scraper = GoogleMapsScraper(queries)
```

## 🛠️ Advanced Configuration

See `config.py` for advanced options:

```python
from config import ScraperConfig

config = ScraperConfig(
    search_queries=["plumbers in New York"],
    min_rating=4.0,  # Only businesses with 4+ stars
    min_reviews=5,   # Only businesses with 5+ reviews
    exclude_keywords=["chain", "corporate"],  # Exclude large companies
)
```

## 📁 Project Structure

```
google-maps-scraper/
├── scraper.py          # Main scraper class
├── config.py           # Configuration dataclass
├── examples.py         # Usage examples
├── requirements.txt    # Python dependencies
├── output/             # Results directory (auto-created)
│   ├── google_maps_businesses_*.json
│   └── google_maps_businesses_*.csv
└── README.md          # This file
```

## ⚠️ Important Notes

### Rate Limiting & Ethics

- **Respect Google's Terms of Service** - Don't overload with requests
- **Add delays between requests** - Use proxy rotation for large-scale scraping
- **Respect robots.txt** - Check if scraping is allowed
- **Use responsibly** - This tool is for legitimate business purposes

### Technical Considerations

- **JavaScript rendering** - Uses Playwright for dynamic content
- **Session management** - Browser sessions are created per crawl
- **Error handling** - Failed requests are automatically retried
- **Headless mode** - Runs without visible browser window

## 🔧 Troubleshooting

### "Browser not found"

```bash
playwright install
```

### Low result counts

- Google Maps limits search results; try more specific queries
- Use different geographic areas
- Increase request timeout in config

### Connection errors

- Check your internet connection
- Try with a VPN or proxy
- Increase request retry count

## 🎯 Use Cases

1. **Lead Generation** - Find SMBs without online presence
2. **Landing Page Creation** - Build sites for businesses lacking web presence
3. **Market Research** - Analyze SMB distribution and categories
4. **CRM Integration** - Export data to sales tools
5. **Competitive Analysis** - Track local business listings

## 📝 License

This project is provided as-is for legitimate business purposes.

## 🤝 Contributing

Feel free to modify and extend the scraper for your needs. Key areas for enhancement:

- Add filtering by business category
- Integrate with CRM APIs
- Add image scraping
- Implement review sentiment analysis
- Create automated landing page generation

## 📧 Support

For issues or questions, refer to:

- Crawlee documentation: https://crawlee.dev
- Playwright documentation: https://playwright.dev
