def is_decimal(s):
    try:
        num = float(s)
        if '.' in s:
            decimal_part = s.split('.')[1]
            if len(decimal_part) > 2:
                return False
        return True
    except ValueError:
        return False

print(is_decimal('123.11')) # should return True
print(is_decimal('123.111')) # should return False
print(is_decimal('123')) # should return True
print(is_decimal('123.1')) # should return True
print(is_decimal('123.1a')) # should return False
print(is_decimal('a123.11')) # should return False
"""

# Solution
def is_decimal(s):
    try:
        num = float(s)
        if '.' in s:
            decimal_part = s.split('.')[1]
            if len(decimal_part) > 2:
                return False
        return True
    except ValueError:
        return False

assert is_decimal('123.11')==True
assert is_decimal('123.111')==False
assert is_decimal('123')==True
assert is_decimal('123.1')==True
assert is_decimal('123.1a')==False
assert is_decimal('a123.11')==False

# End of solution
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 10:Write a function to check whether a given string is a valid mobile number. A valid mobile number is a 10-digit number that starts with 6, 7, 8, or 9.```assert is_valid_mobile_number('9876543210')==Trueassert is_valid_mobile_number('1234567890')==Falseassert is_valid_mobile_number('987654321a')==Falseassert is