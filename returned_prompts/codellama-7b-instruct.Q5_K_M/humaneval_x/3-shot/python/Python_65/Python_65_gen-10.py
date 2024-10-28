    digits = str(x)
    new_digits = []

    for _ in range(shift):
        new_digits.append(digits[-1])
        digits = digits[:-1]

    return ''.join(new_digits + digits)


