def is_decimal(s):
    if '.' in s:
        left, right = s.split('.')
        if len(left) > 3 or len(right) > 2:
            return False
    else:
        if len(s) > 3:
            return False
    return True
# test case
print(is_decimal('123.11')) # True
print(is_decimal('123')) # True
print(is_decimal('123456')) # False
print(is_decimal('123456.123456')) # False
print(is_decimal('123456.123')) # True
print(is_decimal('123456.123456789012')) # False
print(is_decimal('123456.123456789012345')) # False
print(is_decimal('123456.1234567890123456')) # False
print(is_decimal('123456.12345678901234567')) # False
print(is_decimal('123456.123456789012345678')) # False
print(is_decimal('123456.1234567890123456789')) # False
print(is_decimal('123456.12345678901234567890')) # False
print(is_decimal('123456.123456789012345678901')) # False
print(is_decimal('123456.1234567890123456789012')) # False
print(is_decimal('123456.12345678901234567890123')) # False
print(is_decimal('123456.123456789012345678901234')) # False
print(is_decimal('123456.1234567890123456789012345')) # False
print(is_decimal('123456.12345678901234567890123456')) # False
print(is_decimal('123456.123456789012345678901234567')) # False
print(is_decimal('123456.1234567890123456789012345678')) # False
print(is_decimal('123456.12345678901234567890123456789')) # False
print(is_decimal('123456.123456789012345678901234567890')) # False
print(is_decimal('123456.123456789012345678901234567891')) # False
print(is_decimal('123456.123456789012345678901234567892')) # False
print(is_decimal('123456.123456789012345678901234567893')) # False
print(is_decimal('123456.123456789012345678901234