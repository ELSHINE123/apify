"""
Configuration for Google Maps Scraper
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class ScraperConfig:
    """Configuration settings for the scraper"""

    # Search queries to scrape
    search_queries: list[str]

    # Output directory for results
    output_dir: str = "./output"

    # Crawl settings
    max_requests_per_crawl: int = 100
    max_crawl_depth: int = 2
    request_timeout: int = 30000  # milliseconds

    # Business filtering
    # e.g., 3.5 to filter low-rated businesses
    min_rating: Optional[float] = None
    # e.g., 5 to filter newly listed businesses
    min_reviews: Optional[int] = None
    # e.g., ["chain", "corporation"] to exclude large companies
    exclude_keywords: list[str] = None

    # Scraping behavior
    headless: bool = True  # Run browser in headless mode
    proxy_list: Optional[list[str]] = None  # List of proxies to rotate through
    user_agent: Optional[str] = None  # Custom user agent

    def __post_init__(self):
        if self.exclude_keywords is None:
            self.exclude_keywords = []
