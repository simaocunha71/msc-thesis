    digits = str(x)
    if shift >= len(digits):
        return digits[::-1]
    else:
        return digits[-shift:] + digits[:-shift]


