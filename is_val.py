# from validate_email import validate_email
# from process_text import get_emails_and_companies

# email_company_dict = get_emails_and_companies('mail.csv')
# total = len(email_company_dict)
# for no, email in email_company_dict.items():

#     print(validate_email(
#     email_address=email,check_smtp=True,check_format=False,
#     check_dns=False,
#     check_blacklist=False,

# ))
from pythonmonkey import require as js_require
js_lib = js_require('./email-validator')
print(validator.validate("srmeenak@in.ibm.com"))