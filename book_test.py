from price_tracker.services.book_scraper import get_book_price

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

price = get_book_price(url)

print(price)