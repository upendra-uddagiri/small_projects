from dotenv import load_dotenv
from alert_manager import Alerts
from get_price import GetPrice

load_dotenv()

live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

price_fetcher = GetPrice()
alert_manager = Alerts()

price_as_float = price_fetcher.get_current_price(live_url)

if price_as_float is None:
    print("Could not retrieve the current price. Please check the URL or your connection.")
else:
    print(f"Current price: ${price_as_float}")
    target_price = float(input("Enter your target price: "))
    if price_as_float < target_price:
        alert_manager.send_alert(live_url)
    else:
        print(f"Current price (${price_as_float}) is still above your target (${target_price}). No alert sent.")
