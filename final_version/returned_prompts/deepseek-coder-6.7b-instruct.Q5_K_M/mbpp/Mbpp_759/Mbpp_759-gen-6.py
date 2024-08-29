
def is_decimal(s):
    return s.count('.') == 1 and s.replace('.', '', 1).isdigit() and len(s.split('.')[1]) == 2

print(is_decimal('123.11'))

# or

def is_decimal(s):
    try:
        number = float(s)
        return len(s.split('.')[1]) == 2
    except ValueError:
        return False

print(is_decimal('123.11'))

# or

import re

def is_decimal(s):
    return bool(re.fullmatch(r'\d+\.\d{2}', s))

print(is_decimal('123.11'))

# or

import decimal

def is_decimal(s):
    try:
        decimal.Decimal(s)
        return len(str(decimal.Decimal(s)).split('.')[1]) == 2
    except decimal.InvalidOperation:
        return False

print(is_decimal('123.11'))

# or

def is_decimal(s):
    return isinstance(eval(s), float) and len(s.split('.')[1]) == 2 if s.count('.') == 1 and s.replace('.', '', 1).isdigit() else False

print(is_decimal('123.11'))

# or

def is_decimal(s):
    try:
        value = float(s)
        return len(str(value).split('.')[1]) == 2
    except ValueError:
        return False

print(is_decimal('123.11'))
<jupyter_output>
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
True
