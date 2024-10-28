    digits = str(x)
    length = len(digits)

    if length <= shift:
        digits = digits[::-1]

    return digits[shift:] + digits[:shift]


