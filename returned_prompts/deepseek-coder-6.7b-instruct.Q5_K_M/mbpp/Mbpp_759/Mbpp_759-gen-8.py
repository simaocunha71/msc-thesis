def is_decimal(s):
    try:
        float(s)
        if "." in s:
            split_dec = s.split(".")
            if len(split_dec[1]) == 2:
                return True
            else:
                return False
        else:
            return False
    except ValueError:
        return False

# Test Cases
assert is_decimal('123.11')==True
assert is_decimal('123.111')==False
assert is_decimal('123')==False
assert is_decimal('123.')==False
assert is_decimal('123.a1')==False
assert is_decimal('123.1')==False
assert is_decimal('123.111')==False
assert is_decimal('123.11111')==False
assert is_decimal('123.111111')==False
assert is_decimal('123.111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111