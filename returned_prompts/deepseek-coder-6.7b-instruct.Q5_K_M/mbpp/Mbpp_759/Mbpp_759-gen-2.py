def is_decimal(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        if '.' in s:
            return len(s.split('.')[1]) == 2
        else:
            return False

print(is_decimal('123.11'))  # True

"""
