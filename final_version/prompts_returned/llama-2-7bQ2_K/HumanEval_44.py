

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """

    def helper(x: int):
        return str(int(
            x % base ** (1-len(str(x)) * -1) / base, base=base))
    return helper(x)


def convert_string(s: str):
    """Converts a string containing an integer to its numerical value.
    >>> convert_string('7')
    7
    >>> convert_string('02')
    2016
    >>> convert_string('89')
    89
    >>> convert_string('45 2/3')
    45.25
    """

    def helper(s: str):
        return int(str(float(s)))
    return helper(s)

def check_positive():
    """Checks whether a number is positive or not."""
    print (convert_string("89"))  # prints 89 to the console window.
