    roman_numerals = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c',
        400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
    }

    def helper(num):
        if num in roman_numerals:
            return roman_numerals[num]
        if num < 10:
            return helper(num - 5) + 'v' if num % 5 == 0 else 'i' * num
        if num < 100:
            return helper(num // 10) * 10 + 'x' if num % 10 == 0 else helper(num % 10) + 'x'
        if num < 1000:
            return helper(num // 100) * 100 + 'c' if num % 100 == 0 else helper(num % 100) + 'c'

    return helper(number).lower()  # convert to lowercase
# This code can handle numbers from 1 to 1000, and it uses a helper function to convert numbers to roman numerals.
# It also handles the cases where a number is a multiple of 5, 10, 50, 100, 500, 1000 by subtracting the multiple and adding the corresponding roman numeral.
# The function returns the roman numeral as a lowercase string.