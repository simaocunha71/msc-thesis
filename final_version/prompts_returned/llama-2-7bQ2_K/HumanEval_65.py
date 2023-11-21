
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    if (len(str(x)) < shift):
        raise ValueError('shift out of range')
    digits = str(x)[:shift]

    return ''.join([str(i) for i in digits])

# Test the function with some examples.
# The following works, but we've just found a more convenient way to do it.
# >>> circular_shift(1234567890, 3)
# '9976543210'
x = input('Enter an integer: ')
print('Enter any number of digits you like!')
shift = int(input('Enter a shift value (digits in the integer): '))
result = circular_shift(int(x), shift)
print()
for digit in result[::-1]:
    print(digit, end=' ')
