import requests
from bs4 import BeautifulSoup

def get_n11_prices(search_query):
    prices = []
    url = f"https://www.n11.com/arama?q={search_query}&pg=1"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all("li", class_="column")
    for item in items:
        price = item.find("ins").text.replace("TL", "").replace(".", "").replace(",", ".")
        prices.append(float(price))
    lowest_price = min(prices)
    return lowest_price

search_query = input("Lütfen bir arama terimi girin: ")
lowest_price = get_n11_prices(search_query)
if lowest_price is not None:
    print(f"{search_query} ürününün en düşük fiyatı: {lowest_price} TL")
