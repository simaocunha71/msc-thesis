    digits = [str(d) for d in str(x)]
    digits = digits[shift:] + digits[:shift]
    return "".join(digits)


