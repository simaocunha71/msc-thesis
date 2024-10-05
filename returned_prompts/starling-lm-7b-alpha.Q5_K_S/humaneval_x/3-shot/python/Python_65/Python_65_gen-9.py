    digits = str(x)
    if shift <= len(digits):
        return digits[-shift:] + digits[:-shift]
    else:
        return digits[len(digits):] + digits[:len(digits) - shift]


