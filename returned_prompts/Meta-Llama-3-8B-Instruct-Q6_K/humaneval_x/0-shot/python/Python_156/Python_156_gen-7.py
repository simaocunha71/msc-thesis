```
def int_to_mini_roman(number):
    roman_numerals = {1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc', 100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'}
    roman = ''
    for value in sorted(roman_numerals.keys(), reverse=True):
        while number >= value:
            number -= value
            roman += roman_numerals[value]
    return roman.lower()
```


Explanation:
The function `int_to_mini_roman(number)` takes an integer `number` as input and returns its roman numeral equivalent as a string in lowercase.

The dictionary `roman_numerals` is used to map integer values to their corresponding roman numerals. The keys in the dictionary are sorted in descending order to ensure that the largest possible roman numeral is subtracted from the number first.

The function iterates over the sorted keys in the dictionary. For each key, it subtracts the value from the number as many times as possible and appends the corresponding roman numeral to the result string.

Finally, the function returns the result string in lowercase. This ensures that the roman numeral is in the correct case (lowercase) as per the problem statement.

The function works correctly for numbers between 1 and 1000 (inclusive), as specified in the problem statement. For larger numbers, it will not work correctly. If you need to support larger numbers, you will need to modify the function accordingly.