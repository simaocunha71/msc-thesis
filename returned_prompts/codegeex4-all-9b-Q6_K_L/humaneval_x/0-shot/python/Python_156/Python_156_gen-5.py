def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """

    roman_to_int = {
        'i': 1,
        'v': 5,
        'x': 10,
        'l': 50,
        'c': 100,
        'd': 500,
        'm': 1000
    }

    int_to_roman = {
        1000: 'm',
        900: 'cm',
        500: 'd',
        400: 'cd',
        100: 'c',
        90: 'xc',
        50: 'l',
        40: 'xl',
        10: 'x',
        9: 'ix',
        5: 'v',
        4: 'iv',
        1: 'i'
    }

    if number < 1 or number > 1000:
        raise ValueError("Input must be between 1 and 1000.")

    result = ""
    for value, symbol in int_to_roman.items():
        while number >= value:
            result += symbol
            number -= value

    return result.lower()

print(int_to_mini_roman(19))  # Output: xix
print(int_to_mini_roman(152))  # Output: clii
print(int_to_mini_roman(426))  # Output: cdxxvi