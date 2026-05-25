import re

text = "My phone number is 9876543210 and email is test@gmail.com"

# Search for phone number
match = re.search(r'\d{10}', text)

# Find all emails
emails = re.findall(r'\S+@\S+', text)

print("Phone:", match.group())
print("Emails:", emails)
