    digits = list(str(x))
    shift = shift % len(digits)
    return ''.join(digits[-shift:] + digits[:-shift])


