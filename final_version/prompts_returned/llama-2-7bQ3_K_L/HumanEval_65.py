
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if x < 0:
        return '-' + circular_shift(-x,-shift)[::-1]
    else:
        digits = str(format(x, 'b')).split('.')[0][::-1]
        new_digits = []
        for digit in digits[::-1]:
            shifted_digit = shift * int(digit)
            if shift == 0:
                return "0" + str(int(shifted_digit))
            else:
                new_digits.append(str(int(shifted_digit)))
        digits[::-1] = new_digits
        return ''.join(digits)
