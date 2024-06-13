import requests
from bs4 import BeautifulSoup
import csv
import time
from random import randint

# კლასის შექმნა შემდეგი ატრიბუტებით:
# url, გვერდების რაოდენობა, ცარიელი ლისტი ინფორმაციის ჩასაწერად.

class Quotes:
    def __init__(self, url, pages):
        self.url = url
        self.pages = pages
        self.data = []

# request-ის გაგზავნა content-ის წამოსაღებად, ოპერაციის წარმატებულობის შემოწმება.
    def fetch_page(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed Operation, Status code: {response.status_code} ")
            return None

# BeautifulSoup-ის მოდულის საშუალებით კონკრეტული ინფორმაციის წამოღება
    def parse_page(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        for quote in quotes:
            text = quote.span.text
            author = quote.small.text
            self.data.append([text, author])
            # print(text)
            # print(author)

# ინფორმაციის წამოღება მითითებული რაოდენობის გვერდებიდან, ლოგიკური ხანგრძლივობა request-ებს შორის.
    def scrape(self):
        ind = 1
        while ind <= self.pages:
            url = f"{self.url}/page/{ind}/"
            html = self.fetch_page(url)
            if html:
                self.parse_page(html)
            ind += 1
            time.sleep(randint(15,21))

# ინფორმაციის შენახვა csv ფაილში
    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Quote', 'Author'])
            writer.writerows(self.data)
        print(f"Data saved to {filename}")


url = 'https://quotes.toscrape.com'
pages = 5
all_quotes = Quotes(url, pages)

# ყველა quote-ის scrape
all_quotes.scrape()

# შენახვა csv-ში
all_quotes.save_to_csv('quotes.csv')


