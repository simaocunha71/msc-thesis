
The function int_to_mini_roman converts a given integer into its Roman numeral equivalent. The function takes an integer as input, converts it into Roman numerals, and returns the result as a string in lowercase.

The function uses two lists: val and syb. The val list contains the decimal values of the Roman numerals (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1), and the syb list contains the corresponding Roman numeral symbols (M, CM, D, CD, C, XC, L, XL, X, IX, V, IV, I).

The function then iterates over the val and syb lists, appending the Roman numeral symbol to the result string roman_num as many times as the value in val is less than or equal to the input number. It then subtracts the value from the input number. This process continues until the input number becomes 0.

Finally, the function returns the result string roman_num in lowercase.

Here is the code:

```
def int_to_mini_roman(number):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0