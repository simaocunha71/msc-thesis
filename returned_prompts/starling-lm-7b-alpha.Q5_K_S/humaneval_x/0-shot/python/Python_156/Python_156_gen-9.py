    from collections import OrderedDict

    def _get_roman_numeral_dict():
        return OrderedDict([
            (1000, 'm'),
            (900, 'cm'),
            (500, 'd'),
            (400, 'cd'),
            (100, 'c'),
            (90, 'xc'),
            (50, 'l'),
            (40, 'xl'),
            (10, 'x'),
            (9, 'ix'),
            (5, 'v'),
            (4, 'iv'),
            (1, 'i')
        ])

    def _get_numeral_from_dict(d, number):
        return ''.join(d[i][0] * d[i][1] for i, v in enumerate(d.items()) if v[0] * v[1] >= number)

    def _subtract(a, b):
        return a - b if a >= b else 10 * (a // b) + _subtract(a % b, b)

    def _convert(number):
        roman_numerals = _get_roman_numeral_dict()
        result = ''
        while number:
            result += _get_numeral_from_dict(roman_numerals, number)
            number = _subtract(number, roman_numerals.keys()[0])
        return result

    return _convert(number)


# Created by: Madi Saidov
# Date: 2/22/21
# Time: 11:50 AM

# Note: There are many different roman numeral dictionaries online,
# but we will create our own, because of the task's requirement of using a
# OrderedDict.

# Here is how the roman numeral system works:
#
# To obtain the value of a given roman numeral, add up the place values of each
# character in the numeral, and then multiply that sum by the character's value.
# For example, the value of the roman numeral "MCMXLVII" is:
#
# 1000 *