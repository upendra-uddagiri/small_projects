import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

class Alerts:
    def __init__(self):
        self.smtp_email = os.environ["EMAIL_ADDRESS"]
        self.smtp_password = os.environ["EMAIL_PASSWORD"]
        self.recipient_email = os.environ.get("RECIPIENT_EMAIL", self.smtp_email)

    def send_alert(self, url):
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(self.smtp_email, self.smtp_password)
                message = (
                    f"Subject: Low Price Alert!\n\n"
                    f"Your product is under the target price and you can buy it.\n"
                    f"Link: {url}"
                )
                connection.sendmail(
                    from_addr=self.smtp_email,
                    to_addrs=self.recipient_email,
                    msg=message
                )
                print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")