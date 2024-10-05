
    # Define roman numeral equivalents for 1-9
    digits = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']

    # Define roman numeral equivalents for 10-90
    tens = ['x', 'xx', 'xxx', 'xl', 'l', 'lx', 'lxx', 'lxxx', 'xc']

    # Define roman numeral equivalents for 100-900
    hundreds = ['c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dccc', 'cm']

    # Define roman numeral equivalents for 1000
    thousand = 'm'

    # Convert number to roman numeral
    roman_numeral = ''

    # Handle thousands place
    if number // 1000:
        roman_numeral += thousand * (number // 1000)
        number %= 1000

    # Handle hundreds place
    if number // 100:
        roman_numeral += hundreds[number // 100 - 1]
        number %= 100

    # Handle tens place
    if number // 10:
        roman_numeral += tens[number // 10 - 1]
        number %= 10

    # Handle ones place
    if number:
        roman_numeral += digits[number - 1]

    return roman_numeral.lower()

# Test cases
print(int_to_mini_roman(19))  # 'xix'
print(int_to_mini_roman(152))  # 'clii'
print(int_to_mini_roman(426))  # 'cdxxvi'

