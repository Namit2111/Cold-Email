import csv


def get_emails_and_companies(csv_filename):
    email_company_dict = {}
    
    # Open the CSV file
    with open(csv_filename, mode='r') as file:
        # Create a CSV reader
        csv_reader = csv.reader(file)
        
        # Iterate through the rows in the CSV
        for row in csv_reader:
            if len(row) == 2:  # Ensure the row has exactly two elements
                email, company = row
                email_company_dict[email.strip()] = company.strip()
    
    return email_company_dict


