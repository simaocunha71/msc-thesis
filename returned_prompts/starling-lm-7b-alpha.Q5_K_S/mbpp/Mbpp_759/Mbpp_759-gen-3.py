"""
def is_decimal(s):
    if len(s) != 4:
        return False
    if s[0] == '.':
        return False
    if s[2] != '.':
        return False
    if s[3] != '0':
        return False
    if s[1] not in '0123456789':
        return False
    if s[2] not in '0':
        return False
    return True
"""

def is_decimal(s):
    if len(s) != 4:
        return False
    if s[0] == '.':
        return False
    if s[2] != '.':
        return False
    if s[3] != '0':
        return False
    if s[1] not in '0123456789':
        return False
    if s[2] not in '0':
        return False
    return True

def test_is_decimal():
    assert is_decimal('123.11') == True
    assert is_decimal('123') == False
    assert is_decimal('123.111') == False
    assert is_decimal('123.1') == False
    assert is_decimal('123.') == False
    assert is_decimal('.123') == False
    assert is_decimal('123.12') == False
    assert is_decimal('123.110') == False
    assert is_decimal('123.11.') == False

test_is_decimal()

# """
# Write a function to check whether a given string is a decimal number with a precision of 2.
# assert is_decimal('123.11')==True
# """

# def is_decimal(s):
#     if len(s) != 4:
#         return False
#     if s[0] == '.':
#         return False
#     if s[2] != '.':
#         return False
#     if s[