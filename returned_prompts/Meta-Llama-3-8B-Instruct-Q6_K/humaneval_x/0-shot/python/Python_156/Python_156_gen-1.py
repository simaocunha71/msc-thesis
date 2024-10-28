    def int_to_mini_roman(number):
        roman_numerals = {
            1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c', 90: 'xc',
            50: 'l', 40: 'xl', 10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'
        }
        roman_str = ''
        for value, numeral in sorted(roman_numerals.items(), reverse=True):
            while number >= value:
                roman_str += numeral
                number -= value
        return roman_str.lower()  # lowercase roman numeral string
# Test the function
print(int_to_mini_roman(19))  # Expected output: 'xix'
print(int_to_mini_roman(152))  # Expected output: 'clii'
print(int_to_mini_roman(426))  # Expected output: 'cdxxvi'
print(int_to_mini_roman(1000))  # Expected output: 'm' (for 1000)
print(int_to_mini_roman(4))  # Expected output: 'iv'
print(int_to_mini_roman(1))  # Expected output: 'i'
print(int_to_mini_roman(9))  # Expected output: 'ix'
print(int_to_mini_roman(5))  # Expected output: 'v'  # Expected output: 'v'
print(int_to_mini_roman(123))  # Expected output: 'cxxiii'
print(int_to_mini_roman(99))  # Expected output: 'xcix'  # Expected output: 'xcix'
print(int_to_mini_roman(199))  # Expected output: 'xcix'
print(int_to_mini_roman(100))  # Expected output: 'c'
print(int_to_mini_roman(101))  # Expected output: 'ci'
print(int_to_mini_roman(1000))  # Expected output: 'm'  # Expected output: 'm'  # Expected output: 'm'
print(int_to_mini_roman(1001))  # Expected output: 'mi'
print(int_to_mini_roman(1002))  # Expected output: 'mi'  # Expected output: 'mi'
print(int_to_mini_roman(1003))  # Expected output: 'mi'
print(int_to_mini_roman(1004))