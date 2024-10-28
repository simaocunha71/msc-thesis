
def circular_shift(x, shift):
    digits = str(x)
    if shift > len(digits):
        return digits[::-1]
    return digits[shift:] + digits[:shift]
