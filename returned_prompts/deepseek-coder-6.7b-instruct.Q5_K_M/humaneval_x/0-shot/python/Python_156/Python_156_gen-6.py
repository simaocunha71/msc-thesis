
    num_map = [(1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'), 
               (100, 'c'), (90, 'xc'), (50, 'l'), (40, 'xl'), 
               (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')]
    roman = ''
    for i, num in num_map:
        count = int(number / i)
        roman += num * count
        number -= i * count
    return roman

print(int_to_mini_roman(19))
print(int_to_mini_roman(152))
print(int_to_mini_roman(426))
"""

# Python program to convert integer values to Roman Numerals

# Function to generate the Roman numeral equivalent
def int_to_mini_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "m", "cm", "d", "cd",
        "c", "xc", "l", "xl",
        "x", "ix", "v", "iv",
        "i"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

print(int_to_mini_roman(19))
print(int_to_mini_roman(152))
print(int_to_mini_roman(426))

# Output: 
# xix
# clii
# cdxxvi
<jupyter_output>
