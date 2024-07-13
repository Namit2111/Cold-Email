# Bulk Email Sender

This project consists of two main Python scripts, `process_text.py` and `send_mail.py`, designed to read email addresses and company names from a CSV file, and send personalized internship application emails with attachments.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Required libraries: `smtplib`, `email`, `csv`

Additionally, you'll need a CSV file named `Book1.csv` in the same directory, with the following structure:

```
email,company
example@example.com,Example Company
...
```

## Setup

1. Clone the repository to your local machine.
2. Ensure your CSV file (`Book1.csv`) is in the same directory as the scripts.
3. Place your resume file (`Namit_Resume.pdf`) and the email body template (`cold.txt`) in the same directory.

## Scripts

### 1. `process_text.py`

This script reads email addresses and company names from a CSV file and stores them in a dictionary.

#### Usage:

```python
from process_text import get_emails_and_companies

email_company_dict = get_emails_and_companies('Book1.csv')
```

### 2. `send_mail.py`

This script sends personalized emails with an attached PDF resume to the email addresses read from the CSV file. It also includes email validation.

#### Usage:

```python
import os
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from process_text import get_emails_and_companies

my_email_id = 'your_email@gmail.com'
email_pass = 'your_app_password'

def send(email_id, to_email):
    # Function implementation

def main():
    try:
        email_company_dict = get_emails_and_companies('Book1.csv')
        for email in email_company_dict:
            send(my_email_id, email)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

## Running the Scripts

1. Ensure your CSV file (`Book1.csv`), resume file (`Namit_Resume.pdf`), and email body template (`cold.txt`) are in the same directory as the scripts.
2. Run the `send_mail.py` script:

```bash
python send_mail.py
```

The script will read the email addresses and company names from the CSV file, validate the email addresses, and send personalized emails with the resume attached.

## Notes

- Ensure you replace the placeholder email and password in `send_mail.py` with your actual credentials.
- The email body template (`cold.txt`) should be customized to include placeholders for company names if needed.

