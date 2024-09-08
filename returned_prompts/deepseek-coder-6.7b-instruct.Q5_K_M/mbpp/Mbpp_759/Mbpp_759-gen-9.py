def is_decimal(s):
    try:
        float(s)
        if '.' in s:
            decimal_part = s[s.index('.') + 1:]
            if len(decimal_part) == 2:
                return True
        return False
    except ValueError:
        return False

assert is_decimal('123.11') == True
assert is_decimal('123.111') == False
assert is_decimal('123') == False
assert is_decimal('123.') == False
assert is_decimal('123.1') == False
assert is_decimal('123.111') == False
assert is_decimal('abc') == False
assert is_decimal('123.456') == False
assert is_decimal('123.11111') == False
assert is_decimal('123.111111') == False
"""
1. Use try/except to catch any ValueError that occurs when trying to convert the string to a float. If a ValueError is caught, the function returns False.
2. If no ValueError is caught, the function checks if '.' is in the string.
3. If '.' is in the string, the function gets the part of the string after the decimal point.
4. If the length of the part after the decimal point is 2, the function returns True. Otherwise, it returns False.
5. If '.' is not in the string, the function returns False.
"""

#Solution 2
def is_decimal(s):
    import re
    match = re.fullmatch(r"\d+\.\d{2}$", s)
    return True if match else False

assert is_decimal('123.11') == True
assert is_decimal('123.111') == False
assert is_decimal('123') == False
assert is_decimal('123.') == False
assert is_decimal('123.1') == False
assert is_decimal('123.111') == False
assert is_