Price Tracker
A Python-based monitoring tool that tracks Amazon product prices and sends you an email alert when the price drops below your target. This project includes both a simple Command Line Interface (CLI) and a sleek, interactive web interface built with Streamlit.

✨ Features
Real-Time Price Fetching: Scrapes current product prices directly from Amazon using requests and BeautifulSoup.

Email Notifications: Automatically sends an email alert via Gmail's SMTP server (port 587) the moment a price drops below your specified threshold.

Modern Web UI: Features a custom-styled Streamlit app with a dark theme, custom fonts, and a real-time activity log.

Automated Monitoring: The web interface allows you to start an auto-monitor loop, checking the price at configurable intervals (1 min, 5 min, 15 min, 30 min, or 1 hr).

CLI Fallback: A straightforward main.py script for quick terminal-based checks and testing.

🛠️ Prerequisites
Make sure you have Python 3.7+ installed. You will need to install the following dependencies:

Bash
pip install requests beautifulsoup4 python-dotenv streamlit
⚙️ Configuration
Before running the app, you must set up your environment variables for the email alerts to work.

Create a .env file in the root directory of the project.

Add your email credentials to the file.
(Note: Since this uses Gmail, you will likely need to generate an "App Password" in your Google Account settings instead of using your standard password).

Code snippet
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
RECIPIENT_EMAIL=recipient_email@gmail.com 
If RECIPIENT_EMAIL is omitted, the app will default to sending the alert to the sender's EMAIL_ADDRESS.

🚀 Usage
Option 1: The Streamlit Web App (Recommended)
For the full interactive experience with auto-monitoring and visual logs, run the Streamlit app:

Bash
streamlit run app.py
This will open a local web server in your browser where you can paste any Amazon URL, set your target price, and start tracking.

Option 2: Command Line Interface (CLI)
If you prefer the terminal, you can run the main script. By default, it checks a hardcoded URL.

Bash
python main.py
The script will output the current price and prompt you to input a target price. If the current price is lower than your input, an alert will be sent immediately.

🗂️ Project Structure
app.py: The Streamlit frontend containing custom CSS, input forms, and the auto-monitoring logic.

main.py: The terminal-based script to test single URLs and prompt for a target price.

alert_manager.py: Contains the Alerts class, handling the SMTP connection and formatting the email message.

get_price.py: Contains the GetPrice class, which handles HTTP requests to Amazon and parses the HTML to extract the price string.
