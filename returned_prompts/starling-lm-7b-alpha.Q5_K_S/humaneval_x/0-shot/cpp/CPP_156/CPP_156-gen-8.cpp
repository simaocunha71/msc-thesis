
Here's a Python function that accomplishes the same thing:

```python
def int_to_mini_roman(number):
    if number < 1:
        return ""

    roman_numerals = {
        1000: "m", 900: "cm", 500: "d", 400: "cd",
        100: "c", 90: "xc", 50: "l", 40: "xl",
        10: "x", 9: "ix", 5: "v", 4: "iv", 1: "i"
    }

    result = ""
    for key in sorted(roman_numerals, reverse=True):
