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

    # Define the roman numeral symbols and their corresponding values
    roman_nums = {
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

    # Initialize an empty string to store the roman numeral equivalent
    result = ''

    # Iterate over the roman numeral symbols and values
    for value, symbol in roman_nums.items():
        # While the number is greater than or equal to the current value
        while number >= value:
            # Append the corresponding symbol to the result string
            result += symbol
            # Subtract the current value from the number
            number -= value

    # Return the roman numeral equivalent
    return result

# Test the function with the provided examples
print(int_to_mini_roman(19))  # Expected output: 'xix'
print(int_to_mini_roman(152))  # Expected output: 'clii'
print(int_to_mini_roman(426))  # Expected output: 'cdxxvi'