def is_decimal(s):
    if '.' not in s:
        return s.isdigit() and len(s) <= 3
    else:
        left, right = s.split('.')
        return left.isdigit() and len(left) <= 3 and right.isdigit() and len(right) <= 2

assert is_decimal('123.11')==True
assert is_decimal('123')==True
assert is_decimal('12345')==False
assert is_decimal('123.12345')==False
assert is_decimal('123.12')==True
assert is_decimal('123.123')==False
assert is_decimal('123.123456')==False
assert is_decimal('123.1')==True
assert is_decimal('123.12')==True
assert is_decimal('123.12345')==False
assert is_decimal('123.1234567')==False
assert is_decimal('123.12345678')==False
assert is_decimal('123.123456789')==False
assert is_decimal('123.1234567890')==False
assert is_decimal('123.12345678901')==False
assert is_decimal('123.123456789012')==False
assert is_decimal('123.1234567890123')==False
assert is_decimal('123.12345678901234')==False
assert is_decimal('123.123456789012345')==False
assert is_decimal('123.1234567890123456')==False
assert is_decimal('123.12345678901234567')==False
assert is_decimal('123.123456789012345678')==False
assert is_decimal('123.1234567890123456789')==False
assert is_decimal('123.12345678901234567890')==False
assert is_decimal('123.123456789012345678901')==False
assert is_decimal('123.1234567890123456789012')==False
assert is_decimal('123.12345678901234567890123')==False
assert is_decimal('123.123456789012345678901234')==False
assert is_decimal('123.1234567890123456789012345')==False
assert is_decimal('123.12345678901234567890123456')==False
assert is_decimal('123.123456789012345678901234567')==False
assert is_decimal('123.1234567890123456789012345678')==False
assert is_decimal('123.12345678901234567890123456789')==False