# Amazon Price Tracker

Monitors an Amazon product price and sends an email alert when it drops below your target.

---

## Setup

**Install dependencies**
```bash
pip install requests beautifulsoup4 streamlit python-dotenv
```

**Create a `.env` file**
```
EMAIL_ADDRESS=you@gmail.com
EMAIL_PASSWORD=your_app_password
RECIPIENT_EMAIL=recipient@gmail.com  # optional, defaults to EMAIL_ADDRESS
```

> Gmail requires an [App Password](https://myaccount.google.com/apppasswords), not your regular account password.

---

## Usage

**CLI**
```bash
python main.py
```
Enter the product URL and target price when prompted. An alert is sent immediately if the price is below your target.

**Streamlit UI**
```bash
streamlit run app.py
```
- Check price instantly with a single click
- Auto-monitor at a set interval (1 min – 1 hr)
- Live activity log and alert status

---

## Project Structure

| File | Description |
|------|-------------|
| `get_price.py` | Scrapes the current price from Amazon |
| `alert_manager.py` | Sends email alert via Gmail SMTP |
| `main.py` | CLI entry point |
| `app.py` | Streamlit web UI |
| `.env` | Email credentials (do not commit) |

---

## Notes

- Amazon may block automated requests. Avoid rapid successive checks.
- The price element class (`a-offscreen`) may vary by product — inspect the page source if prices aren't detected.
- Automated scraping may conflict with Amazon's Terms of Service. Use for personal purposes only.
