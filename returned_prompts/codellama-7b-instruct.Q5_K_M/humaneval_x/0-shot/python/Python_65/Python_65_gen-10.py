
def circular_shift(x, shift):
    n = str(x)
    n = n[shift:] + n[:shift]
    return n
