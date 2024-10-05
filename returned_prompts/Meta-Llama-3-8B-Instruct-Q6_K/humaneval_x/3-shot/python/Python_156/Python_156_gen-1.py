    roman_numerals = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l',
        90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
    }

    def int_to_roman(n):
        result = ''
        for value, numeral in sorted(roman_numerals.items(), reverse=True):
            while n >= value:
                n -= value
                result += numeral
        return result.lower()

    return int_to_roman(number)  # Note: We don't need to add the 'mini' part in the output. It's just a hint.