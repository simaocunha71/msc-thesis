    digits = str(x)
    new_digits = digits[-shift:] + digits[:-shift]
    return ''.join(new_digits)


