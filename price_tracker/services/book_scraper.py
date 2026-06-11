import requests
from bs4 import BeautifulSoup


def scrape_books():

    url = "https://books.toscrape.com"

    response = requests.get(url)
    response.encoding = "utf-8"

    soup = BeautifulSoup(
        response.text,
        "lxml"
    )

    books = soup.find_all("article")

    products = []

    for book in books:

        title = book.find(
            "h3"
        ).find("a")["title"]

        price = book.find(
            "p",
            class_="price_color"
        ).text.strip()

        products.append(
            {
                "title": title,
                "price": price
            }
        )

    return products