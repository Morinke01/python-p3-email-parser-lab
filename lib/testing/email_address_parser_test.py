from email_address_parser import EmailAddressParser

class TestEmailAddressParser:
    # Test if EmailAddressParser instantiates with a string
    def test_instantiates_with_string(self):
        email_parser = EmailAddressParser("string string@string.com, mr. string, iamastring@icloud.com")
        assert isinstance(email_parser, EmailAddressParser)

    # Test if EmailAddressParser has a parse method
    def test_has_parse_method(self):
        email_parser = EmailAddressParser("dummy string")
        assert hasattr(email_parser, "parse")

    # Test if EmailAddressParser correctly parses emails with spaces
    def test_parses_emails_with_spaces(self):
        email_string = "talk@talk.com john.jones@flatironschool.com alexa@amazon.com"
        parser = EmailAddressParser(email_string)
        parsed_emails = parser.parse()
        expected_emails = ["talk@talk.com", "john.jones@flatironschool.com", "alexa@amazon.com"]
        assert parsed_emails == expected_emails

    # Test if EmailAddressParser correctly parses emails with commas
    def test_parses_emails_with_commas(self):
        email_string = "talk@talk.com,john.jones@flatironschool.com,alexa@amazon.com"
        parser = EmailAddressParser(email_string)
        parsed_emails = parser.parse()
        expected_emails = ["talk@talk.com", "john.jones@flatironschool.com", "alexa@amazon.com"]
        assert parsed_emails == expected_emails

    # Test if EmailAddressParser correctly parses emails with commas and spaces
    def test_parses_emails_with_commas_and_spaces(self):
        email_string = "talk@talk.com, john.jones@flatironschool.com, alexa@amazon.com"
        parser = EmailAddressParser(email_string)
        parsed_emails = parser.parse()
        expected_emails = ["talk@talk.com", "john.jones@flatironschool.com", "alexa@amazon.com"]
        assert parsed_emails == expected_emails

    # Test if EmailAddressParser correctly parses emails, removes non-email strings
    def test_parses_emails_with_commas_and_spaces_and_non_emails(self):
        email_string = "talk@talk.com, what john.jones@flatironschool.com, who alexa@amazon.com, where when why"
        parser = EmailAddressParser(email_string)
        parsed_emails = parser.parse()
        expected_emails = ["talk@talk.com", "john.jones@flatironschool.com", "alexa@amazon.com"]
        assert parsed_emails == expected_emails
