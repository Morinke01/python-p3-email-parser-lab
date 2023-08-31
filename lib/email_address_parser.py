import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string
    
    def parse(self):
        # Regular expression pattern to match email addresses
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        # Use re.findall() to find all email addresses in the string
        email_addresses = re.findall(email_pattern, self.email_string)
        
        return email_addresses


# Example usage
email_string = "alexa@amazon.com talk@talk.com john.jones@flatironschool.com"
parser = EmailAddressParser(email_string)
parsed_emails = parser.parse()
print(parsed_emails)
