
Here's a solution in Python:

```python
def intToMiniRoman(number):
    roman_numerals = {
        1000: 'm',
        900: 'cm',
        500: 'd',
        400: 'cd',
        100: 'c',
        90: 'xc',
        50: 'l',
        40: 'xl',
        10: 'x',
        9: 'ix',
        5: 'v',
        4: 'iv',
        1: 'i'
    }
    result = ''
    for key, symbol in roman_numerals.items():
        count = number // key
        result += symbol * count
        number -= count * key
    return result
```

This solution defines a dictionary called `roman_numerals` that maps each decimal integer to its corresponding Roman numeral symbol. Then, it initializes an empty string called `result` to store the final result. The solution uses a `for` loop to iterate through the `roman_numerals` dictionary in descending order of keys. For each key-symbol pair, it calculates the count of that symbol by dividing the current `number` by the key. It then appends the symbol to the `result` string `count` number of times and subtracts the count of the key from the `number`. Finally, the solution returns the `result` string, which represents the Roman numeral equivalent of the input `number`.

To use this solution, you can call the `intToMiniRoman` function with a positive integer as the argument. For example, `intToMiniRoman(19)` will return the string `'xix'`, `intToMiniRoman(152)` will return `'clii'`, and `intToMiniRoman(426)` will return `'cdxxvi'`.

This solution adheres to the restrictions and examples provided in the question.
```

Here's a solution in Python:

```python
def intToMiniRoman(number):
    roman_numerals = {
        1000: 'm',
        900