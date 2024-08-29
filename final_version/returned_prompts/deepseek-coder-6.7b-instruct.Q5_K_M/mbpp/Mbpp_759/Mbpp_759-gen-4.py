def is_decimal(s):
    if "." in s:
        parts = s.split('.')
        if len(parts) != 2:
            return False
        if not parts[0].isdigit() or not parts[1].isdigit():
            return False
        if len(parts[1]) > 2:
            return False
    else:
        if not s.isdigit():
            return False
    return True

assert is_decimal('123.11') == True
assert is_decimal('123.111') == False
assert is_decimal('123.') == False
assert is_decimal('.11') == False
assert is_decimal('123') == True
assert is_decimal('123.1') == True
assert is_decimal('123.123') == False
assert is_decimal('123.123') == False
assert is_decimal('123.1a') == False
assert is_decimal('123a.11') == False
assert is_decimal('123.a1') == False
assert is_decimal('a123.11') == False
assert is_decimal('123.11a') == False
assert is_decimal('123.111') == False
assert is_decimal('123.1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111