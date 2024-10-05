    # Roman numerals in lowercase
    numerals = {
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

    # Create a dictionary to store the values of each digit in the number
    value_dict = {}
    for digit in reversed(str(number)):
        if digit in value_dict:
            value_dict[digit] += 1
        else:
            value_dict[digit] = 1

    # Initialize a string to store the roman numeral
    roman = ''

    # Iterate over the numerals dictionary, adding roman numerals based on the number
    # of each value in the value_dict
    for numeral, value in numerals.items():
        while value_dict and value_dict[str(value)[0]] >= value:
            roman += str(value) * value_dict[str(value)[0]]
            value_dict[str(value)[0]] = 0
    return roman

# Run tests
...

# End tests























































































































































































