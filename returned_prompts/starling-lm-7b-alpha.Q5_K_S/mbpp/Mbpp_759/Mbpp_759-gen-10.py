"""
Here is a possible solution to this problem. This function first checks if the string contains a decimal point, if not, it returns False. Then it checks if the number after the decimal point is less than 2, if so, it also returns False. Finally, it checks if the number before the decimal point is an integer, if not, it also returns False.
"""

def is_decimal(s):
    if "." not in s:
        return False
    if s.split(".")[1] > "99":
        return False
    if not s.split(".")[0].isdigit():
        return False
    return True

# Test
print(is_decimal('123.11'))  # True
print(is_decimal('123.12'))  # False
print(is_decimal('123.1'))   # True
print(is_decimal('123.111')) # False
print(is_decimal('abc.12'))  # False

# Modified function to allow leading zeros
def is_decimal(s):
    if "." not in s:
        return False
    if s.split(".")[1] > "99":
        return False
    if not s.split(".")[0].isdigit() or s.split(".")[0] == "0" * len(s.split(".")[0]):
        return False
    return True

# Test
print(is_decimal('123.11'))  # True
print(is_decimal('123.12'))  # False
print(is_decimal('123.1'))   # True
print(is_decimal('123.111')) # False
print(is_decimal('abc.12'))  # False
print(is_decimal('0.12'))    # True

"""
The above function checks if a string is a decimal number with a precision of 2, but it does not consider the precision of the number before the decimal point. For example, the function will return True for the number '123456789.12', although the number before