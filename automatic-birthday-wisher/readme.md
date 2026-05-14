# 🎂 Automated Birthday Email Sender (Python)

This project is a simple **Python automation script** that checks for birthdays from a CSV file and automatically sends a personalized birthday email using SMTP.

It selects a random letter template, replaces the recipient’s name, and sends the message via Gmail.

---

## 🚀 Features

* Reads birthday data from a CSV file
* Checks if today matches any birthday
* Picks a random birthday letter template
* Automatically personalizes the message
* Sends email using Gmail SMTP

---

## 🛠️ Technologies Used

* Python
* Pandas (for CSV handling)
* smtplib (for sending emails)
* datetime
* random

---

## 📂 Project Structure

```
project/
│── main.py
│── birthdays.csv
│── letter_templates/
│    ├── letter_1.txt
│    ├── letter_2.txt
│    └── letter_3.txt
```

---

## 📄 CSV Format

Your `birthdays.csv` file should follow this structure:

```
name,email,year,month,day
Tony,tony@gmail.com,1999,6,21
Steve,steve@gmail.com,1998,2,14
```

---

## ⚙️ Setup Instructions

1. Install dependencies

```
pip install pandas
```

2. Enable **Less Secure Apps / App Password** in Gmail
   (Recommended: Use **App Password**, not your real password)

3. Update these fields in `main.py`:

```
MY_EMAIL = "your_email@gmail.com"
MY_PASSWORD = "your_app_password"
```

4. Run the script:

```
python main.py
```

---

## 🤖 How It Works

1. The script reads the CSV file.
2. It checks if today matches any birthday.
3. If a match is found:

   * A random letter template is selected
   * The name placeholder is replaced
   * Email is sent automatically

---

## 📌 Future Improvements

* Add scheduling with cron / task scheduler
* Add GUI interface
* Add WhatsApp/Telegram notifications
* Support multiple email providers



Give it a star on GitHub and feel free to improve it!
