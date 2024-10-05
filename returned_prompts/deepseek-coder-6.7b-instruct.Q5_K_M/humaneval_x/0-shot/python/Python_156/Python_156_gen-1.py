
    roman_numerals = {1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c',
                      90: 'xc', 50: 'l', 40: 'xl', 10: 'x', 9: 'ix',
                      5: 'v', 4: 'iv', 1: 'i'}

    result = ''
    for key in sorted(roman_numerals.keys(), reverse=True):
        while number >= key:
            result += roman_numerals[key]
            number -= key

    return result


# Test cases
print(int_to_mini_roman(19))  # 'xix'
print(int_to_mini_roman(152))  # 'clii'
print(int_to_mini_roman(426))  # 'cdxxvi'


# This code works by creating a dictionary of roman numerals and their corresponding values. It then iterates over this dictionary in descending order.
# For each key, it checks if the input number is greater than or equal to the key. If it is, it appends the corresponding roman numeral to the result and subtracts the key from the number.
# It continues to do this until the number is less than the key. It then moves on to the next key and repeats the process until the number is 0.
# The result is the roman numeral equivalent of the input number.

# This solution assumes that the input number is a valid integer between 1 and 1000 (inclusive). If the input number is not within this range, the function will not work correctly.
# Also, it assumes that the input number is an integer. If the input is not an integer, the function will not work correctly.
# The function also assumes that the input number is always a non-negative integer. If the input number is negative, the function will not work correctly.
# The function also assumes that the input number is a non-zero integer. If the input number is 0, the function will not work correctly.

# However, this code should work for all valid inputs as