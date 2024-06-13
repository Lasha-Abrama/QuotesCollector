# QuotesCollector
The Quote Collector is a Python script designed to scrape quotes from the website quotes.toscrape.com. The script fetches quotes from multiple pages of the website and saves them to a CSV file. It uses the requests library to make requests and BeautifulSoup from the bs4 library to parse HTML content. To avoid overwhelming the server with requests, the script introduces a random delay between fetching each page.

Requirements include Python 3.x, the requests library, and the BeautifulSoup library(for a logical delay time and random modules).
