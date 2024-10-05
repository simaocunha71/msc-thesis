```
def int_to_mini_roman(number):
    if not isinstance(number, int) or number < 1 or number > 1000:
        raise ValueError("Input must be a positive integer between 1 and 1000")

    roman = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c', 90: 'xc', 50: 'l', 
        40: 'xl', 10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'
    }
    result = ''
    for value, roman_value in sorted(roman.items(), reverse=True):
        while number >= value:
            number -= value
            result += roman_value
    return result.lower()
```



The provided Python function, `int_to_mini_roman`, takes a positive integer between 1 and 1000 as input and returns its equivalent Roman numeral string in lowercase.

Here's a step-by-step breakdown of the function:

1. **Input validation**: The function checks if the input `number` is an integer, and if it's within the range of 1 to 1000. If not, it raises a `ValueError`.

2. **Roman numeral dictionary**: The function defines a dictionary `roman` that maps integer values to their corresponding Roman numerals. The dictionary is sorted in descending order by value.

3. **Conversion loop**: The function iterates over the `roman` dictionary, and for each value, it subtracts the value from the input `number` as many times as possible, appending the corresponding Roman numeral to the `result` string each time.

4. **Return the result**: Finally, the function returns the `result` string in lowercase.

The function handles numbers up to 1000, and it correctly converts them to their Roman numeral equivalents. For example, `int_to_mini_roman(19)` returns `'xix'`, `int_to_mini_roman(152)` returns `'clii'`, and `int_to_mini_roman(426)` returns `'cdxxvi'`.