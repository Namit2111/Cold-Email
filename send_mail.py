import os
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from process_text import get_emails_and_companies
# from validate_email import validate_email   csn be use to validate email before sending email
my_email_id = 'namitjainjob2111@gmail.com'
email_pass = 'tzethlzweqpxhokr'

def send(email_id,to_email):
    msg = MIMEMultipart()
    msg['Subject'] = 'Internship Application for Engineering Department'
    msg['From'] = email_id
    msg['To'] = to_email
    # msg.set_content('Hello')
    with open("cold.txt", "r") as file:
        # file_content = file.read().replace('[Company Name]', company)
        file_content = file.read()

# Attach the file content as the email body
    # msg.attach(MIMEText(file_content, "plain"))
    # msg.set_content(file_content)
    # msg.attach(MIMEText(file_content, "plain"))
    body = MIMEText(file_content, "plain")
    msg.attach(body)
 
    pdf_file = "Namit_Resume.pdf"  # Replace with your actual PDF file path
    with open(pdf_file, "rb") as f:
        attachment = MIMEApplication(f.read(), _subtype="pdf")
        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(pdf_file))
    msg.attach(attachment)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_id, email_pass)
        smtp.send_message(msg)

def main():
    try:
        email_company_dict = get_emails_and_companies('Book1.csv')
        total = len(email_company_dict)
        for no, email in email_company_dict.items():
            my_email_id = 'namitjainjob2111@gmail.com'
            is_valid = validate_email(
    email_address=email,check_smtp=True,check_format=False,
    check_dns=False,
    check_blacklist=False)
            if is_valid:  
                send(my_email_id,email)
                total = total -1
                print(f"Email sent to {email} . Remanining: {total}", end="\n")
            else:
                total = total -1
                print(f"Email '{email}' is not valid.")
            
            
            

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
