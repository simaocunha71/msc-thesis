import re
def is_decimal(n):
    # Check if the string is a number
    if not n.isdigit():
        return False

    # Check if the string contains a decimal point
    if '.' not in n:
        return False

    # Check if the string has a precision of 2
    if n.count('.') > 1:
        return False

    # Check if the string has a precision of 2
    if len(n.split('.')[-1]) > 2:
        return False

    return True