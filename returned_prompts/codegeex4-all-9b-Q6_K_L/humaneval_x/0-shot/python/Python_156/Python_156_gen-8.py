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
    # Define the roman numeral equivalents of numbers 1-10
    roman_numerals = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xc',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000: 'm'
    }

    # Initialize the result string
    result = ''

    # Iterate through the roman_numerals dictionary in descending order
    for value, symbol in sorted(roman_numerals.items(), reverse=True):
        # Append the symbol to the result string the number of times equal to the integer division of number by value
        result += symbol * (number // value)
        # Update the number to the remainder of the division
        number %= value

    return result.lower()