    int_to_mini_roman_dict = {
        1: 'i',
        2: 'ii',
        3: 'iii',
        4: 'iv',
        5: 'v',
        6: 'vi',
        7: 'vii',
        8: 'viii',
        9: 'ix',
        10: 'x',
        11: 'xi',
        12: 'xii',
        13: 'xiii',
        14: 'xiv',
        15: 'xv',
        16: 'xvi',
        17: 'xvii',
        18: 'xviii',
        19: 'xix',
        20: 'xx',
        30: 'xxx',
        40: 'xl',
        50: 'l',
        60: 'lx',
        70: 'lxx',
        80: 'lxxx',
        90: 'xc',
        100: 'c',
        200: 'cc',
        300: 'ccc',
        400: 'cd',
        500: 'd',
        600: 'dc',
        700: 'dcc',
        800: 'dccc',
        900: 'cm',
        1000: 'm',
    }

    roman_num = ''
    while number > 0:
        for key, value in int_to_mini_roman_dict.items():
            if number >= key:
                number -= key
                roman_num += value
                break

    return roman_num


