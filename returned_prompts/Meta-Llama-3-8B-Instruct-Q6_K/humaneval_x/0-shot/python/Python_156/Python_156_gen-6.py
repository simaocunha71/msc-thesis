    roman_numerals = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l',
        90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
    }
    roman = ''
    for value in sorted(roman_numerals.keys(), reverse=True):
        while number >= value:
            number -= value
            roman += roman_numerals[value]
    return roman.lower() if roman else 'i'  # Handle the edge case of 1


# Testing
print(int_to_mini_roman(19) == 'xix')  # True
print(int_to_mini_roman(152) == 'clii')  # True
print(int_to_mini_roman(426) == 'cdxxvi')  # True
print(int_to_mini_roman(1) == 'i')  # True
print(int_to_mini_roman(1000) == 'm')  # True
print(int_to_mini_roman(4) == 'iv')  # True
print(int_to_mini_roman(5) == 'v')  # True
print(int_to_mini_roman(9) == 'ix')  # True
print(int_to_mini_roman(10) == 'x')  # True
print(int_to_mini_roman(40) == 'xl')  # True
print(int_to_mini_roman(90) == 'xc')  # True
print(int_to_mini_roman(500) == 'd')  # True
print(int_to_mini_roman(900) == 'cm')  # True
print(int_to_mini_roman(1) == 'i')  # True
print(int_to_mini_roman(100) == 'c')  # True
print(int_to_mini_roman(400) == 'cd')  # True
print(int_to_mini_roman(1000) == 'm')  # True
print(int_to_mini_roman(1234) == 'mccxxxiv')  # True
print(int_to_mini_roman(1999) == 'mcmxcix')  # True
print(int_to_mini_roman(100) == 'c')  # True
print(int_to_mini_roman(199