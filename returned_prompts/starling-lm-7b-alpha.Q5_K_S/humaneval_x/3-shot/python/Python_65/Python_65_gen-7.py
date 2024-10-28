    digits = str(x)
    if len(digits) <= shift:
        return digits[::-1]
    return digits[shift:] + digits[:shift]


