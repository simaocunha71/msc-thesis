
    # Initialize list of roman numerals
    roman_numerals = [
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
    ]

    # Initialize result
    result = ''

    # For each numeral in the list
    for value, numeral in roman_numerals:
        # While the number is greater than or equal to the value of the numeral
        while number >= value:
            # Add the numeral to the result
            result += numeral
            # Subtract the value of the numeral from the number
            number -= value

    # Return the result
    return result

# Test cases
print(int_to_mini_roman(19))  # 'xix'
print(int_to_mini_roman(152))  # 'clii'
print(int_to_mini_roman(426))  # 'cdxxvi'
```

This solution works by iterating over a list of tuples, where each tuple contains a value and its corresponding roman numeral. For each numeral in the list, the solution checks if the input number is greater than or equal to the value of the numeral. If it is, the numeral is added to the result and the value of the numeral is subtracted from the number. The process is repeated until the number becomes 0.

This solution is efficient because it iterates over the list of numerals only once, and the number of numerals is fixed (13). Therefore, the time complexity of the solution is O(1), and the space complexity is also O(1), since the space used does not grow with the size of the input.
"""


def int_to_mini_roman(number):
    roman_numerals