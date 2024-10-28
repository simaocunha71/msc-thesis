    digits = str(x)

    if len(digits) == 1:
        return digits

    shift = shift % len(digits)

    if shift == 0:
        return digits

    return digits[-shift:] + digits[:-shift]


