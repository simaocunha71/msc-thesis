```
def int_to_mini_roman(number):
    roman_numerals = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x',
        40: 'xl', 50: 'l', 90: 'xc', 100: 'c',
        400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
    }
    roman = ''
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while number >= value:
            roman += numeral
            number -= value
    return roman.lower()
```



The function `int_to_mini_roman(number)` takes a positive integer as input and returns its Roman numeral equivalent as a lowercase string.

The function works by iterating over the Roman numerals in descending order, and adding the numeral to the result string as many times as possible without exceeding the input number. This is done using a while loop that subtracts the current value from the input number until it is no longer possible.

The Roman numerals are stored in a dictionary, `roman_numerals`, where the keys are the integer values and the values are the corresponding Roman numerals. This dictionary is used to look up the correct Roman numeral to add to the result string.

The function returns the result string in lowercase using the `lower()` method.

The function works correctly for input numbers between 1 and 1000, as specified in the problem statement. For larger input numbers, the function will still work correctly, but it may not produce the most efficient or readable Roman numeral representation. For example, the input number 1001 would be represented as "mi", which may not be the most readable or efficient representation. To handle larger input numbers, a more complex algorithm would be needed.