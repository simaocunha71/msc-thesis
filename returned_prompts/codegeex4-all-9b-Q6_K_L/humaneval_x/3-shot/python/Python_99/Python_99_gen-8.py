    import math

    if value.isdigit():
        return int(value)

    if '.' not in value:
        return int(value)

    integer_part, decimal_part = value.split('.')
    decimal_part = int(decimal_part)

    if decimal_part >= 5:
        return int(integer_part) + 1 if integer_part[0] != '-' else int(integer_part) - 1
    else:
        return int(integer_part)

