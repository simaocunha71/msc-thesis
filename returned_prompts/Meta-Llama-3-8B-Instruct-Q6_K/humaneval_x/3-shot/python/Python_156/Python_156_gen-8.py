    roman_numerals = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c', 90: 'xc', 50: 'l',
        40: 'xl', 10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'
    }
    result = ''
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while number >= value:
            number -= value
            result += numeral
    return result.lower() if result else 'i'  # if number is 0, return 'i'


