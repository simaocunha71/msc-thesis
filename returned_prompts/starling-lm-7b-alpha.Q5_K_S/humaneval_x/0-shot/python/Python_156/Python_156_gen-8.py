    # We can start by defining the roman numerals in a dictionary
    # The keys are the integer values, and the values are the roman equivalents
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

    # To convert an integer to its roman numeral equivalent, we'll have to use a while loop
    # This loop will keep track of the largest roman numeral we can subtract from the integer
    # We start with the largest roman numeral, 1000, and keep going down the list until we can't subtract any more
    # When we can't subtract any more, we append the roman numeral to the result
    # We then subtract the largest roman numeral from the integer, and keep going down the list until we can't subtract any more
    # We repeat this process until the integer becomes zero
    result = ""
    for place_value, symbol in sorted(roman_numerals.items(), reverse=True):
        while number >= place_value:
            result += symbol
            number -= place_value
    return result

# To test the function, we can use the following doctest
if __name__ == '__main__':
    import doctest
    doctest.testmod()




























































































































