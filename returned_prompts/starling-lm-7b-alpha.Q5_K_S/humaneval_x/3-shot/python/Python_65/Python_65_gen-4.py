    digits = [int(x) for x in str(x)]
    if shift > len(digits):
        digits = digits[::-1]
    else:
        digits = digits[len(digits)-shift:] + digits[:len(digits)-shift]
    return ''.join(str(digit) for digit in digits)


