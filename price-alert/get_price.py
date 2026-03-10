import requests
from bs4 import BeautifulSoup

class GetPrice:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Connection": "keep-alive",
        }

    def get_current_price(self, live_url):
        try:
            response = requests.get(url=live_url, headers=self.headers)
            if response.status_code != 200:
                print(f"Failed to fetch page. Status code: {response.status_code}")
                return None
            soup = BeautifulSoup(response.content, "html.parser")
            price_tag = soup.find(class_="a-offscreen")
            if not price_tag:
                print("Price element not found on page.")
                return None
            price = price_tag.get_text()
            price_as_float = float(price.split(",")[1])
            return price_as_float
        except Exception as e:
            print(f"Error fetching price: {e}")
            return None


