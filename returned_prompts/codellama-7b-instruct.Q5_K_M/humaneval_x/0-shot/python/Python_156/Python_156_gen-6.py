
def int_to_mini_roman(number):
    roman = {
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
    roman_num = ''
    while number > 0:
        for key in sorted(roman.keys(), reverse=True):
            if number >= key:
                roman_num += roman[key]
                number -= key
                break
    return roman_num
