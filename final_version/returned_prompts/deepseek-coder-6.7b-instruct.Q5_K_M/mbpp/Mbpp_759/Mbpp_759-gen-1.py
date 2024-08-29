
def is_decimal(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        if '.' in s:
            split_dec = s.split('.')
            if len(split_dec[1]) != 2:
                return False
        return True

print(is_decimal('123.11'))

# Task 2
