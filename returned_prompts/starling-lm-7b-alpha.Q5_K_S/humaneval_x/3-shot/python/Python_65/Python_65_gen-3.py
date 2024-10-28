    digits = str(x)
    if shift > len(digits):
        digits = digits[::-1]
    else:
        digits = digits[-shift:] + digits[:-shift]
    return int(digits)


