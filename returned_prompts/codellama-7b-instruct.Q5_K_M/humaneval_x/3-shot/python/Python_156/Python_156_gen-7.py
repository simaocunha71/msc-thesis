    roman_numeral_map = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xcix',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000: 'm',
    }

    result = ''
    for place_value, roman_numeral in roman_numeral_map.items():
        while number >= place_value:
            result += roman_numeral
            number -= place_value

    return result


