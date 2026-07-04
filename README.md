# scrape

A small Python scraper that pulls the top-voted stories from [Hacker News](https://news.ycombinator.com/) and prints them ranked by score. It filters out anything below 100 points so you only see the stories that gained real traction.

## How it works

The script requests a Hacker News page, parses it with BeautifulSoup, and pairs each story title and link with its vote count. Stories above the 100-point threshold are collected and sorted highest-first.

## Usage

```bash
pip install requests beautifulsoup4
python hacker_news.py        # scrape page 1
python hacker_news.py 2      # scrape page 2
```

Output is one dictionary per story with its title, link, and score:

```
{'Title': 'Show HN: ...', 'Link': 'https://...', 'Score': 412}
{'Title': '...', 'Link': 'https://...', 'Score': 287}
```

## Notes

The 100-point threshold is hard-coded in `create_custom_news`; adjust it there if you want a different cut-off. HTML scraping depends on Hacker News's current markup, so the selectors may need updating if the site changes.
