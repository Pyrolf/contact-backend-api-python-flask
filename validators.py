import re

def is_email(email):
    return re.match(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", email)

def is_phone_number(phone_number):
    return re.match(r"\+65[6|8|9]\d{7}", phone_number)
