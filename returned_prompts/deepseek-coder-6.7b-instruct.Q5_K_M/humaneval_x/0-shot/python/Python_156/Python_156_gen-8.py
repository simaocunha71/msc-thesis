
    def int_to_mini_roman(number):
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

        result = ''
        for key in sorted(roman_numerals.keys(), reverse=True):
            while number >= key:
                result += roman_numerals[key]
                number -= key
        return result

print(int_to_mini_roman(19))  # 'xix'
print(int_to_mini_roman(152))  # 'clii'
print(int_to_mini_roman(426))  # 'cdxxvi'


Explanation:
We first create a dictionary, roman_numerals, that maps each number between 1 and 1000 to its corresponding roman numeral. We start by trying to subtract the largest possible number (1000) from the given number as many times as possible. We add the corresponding roman numeral to our result string as many times as we subtract it from the number. We continue this process with the next largest number (900), then (500), then (400), and so on, until we have subtracted all possible numbers. The result string is then returned.
"""

# %%
# Q2:
"""
