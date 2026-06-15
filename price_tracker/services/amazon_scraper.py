import requests
from bs4 import BeautifulSoup


def get_amazon_price(url):

    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(
        url,
        headers=headers
    )

    print(response.status_code)

    soup = BeautifulSoup(
        response.text,
        "lxml"
    )

    print(soup.prettify()[:5000])

    return None