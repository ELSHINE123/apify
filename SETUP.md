# Setup and Installation Guide

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Internet connection

## Installation Steps

### 1. Install Python Dependencies

```bash
cd google-maps-scraper
pip install -r requirements.txt
```

This will install:

- **Crawlee** - Web scraping framework
- **Playwright** - Headless browser automation
- **BeautifulSoup4** - HTML parsing
- **Pandas** - Data manipulation (optional, for CSV export)

### 2. Install Playwright Browsers

```bash
playwright install
```

This downloads the necessary browser binaries for Playwright.

### 3. (Optional) Create a Virtual Environment

For better dependency isolation:

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

## Quick Test

To verify installation works:

```bash
python -c "from scraper import GoogleMapsScraper; print('✅ Installation successful!')"
```

## Running Your First Scrape

### Option 1: Using Examples

```bash
python examples.py
```

Edit `examples.py` and uncomment one of the example functions to run.

### Option 2: Custom Script

Create `my_scraper.py`:

```python
import asyncio
from scraper import GoogleMapsScraper

async def main():
    queries = ["plumbers in New York"]
    scraper = GoogleMapsScraper(queries)

    print("Starting scrape...")
    businesses = await scraper.scrape_google_maps()

    scraper.save_results()
    scraper.save_csv()
    scraper.print_summary()

asyncio.run(main())
```

Then run:

```bash
python my_scraper.py
```

## Troubleshooting

### Error: "playwright not found"

```bash
pip install playwright
playwright install
```

### Error: "Module 'crawlee' not found"

```bash
pip install --upgrade crawlee
```

### Low results / timeouts

- Check your internet connection
- Try simpler search queries
- Increase timeout values in scraper.py

### Permission denied (on macOS/Linux)

```bash
chmod +x scraper.py
```

## Output Location

Results are saved to:

```
google-maps-scraper/
└── output/
    ├── google_maps_businesses_YYYYMMDD_HHMMSS.json
    └── google_maps_businesses_YYYYMMDD_HHMMSS.csv
```

## Next Steps

1. Customize search queries in `examples.py`
2. Adjust filtering criteria (rating, reviews, etc.)
3. Integrate with your workflow
4. See `advanced_examples.py` for more patterns

## API Usage

See [Crawlee Documentation](https://crawlee.dev) for advanced features like:

- Proxy management
- Session handling
- Custom middleware
- Data validation
