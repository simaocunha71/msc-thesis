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
    while  number > 0:
        for _ in range(number // val[i]):
            roman_num += syb[i]
            number -= val[i]
        i += 1
    return roman_num.lower()
```


Explanation:

The function `int_to_mini_roman` takes an integer as input and converts it to a Roman numeral. The function uses two lists: `val` and `syb`. The `val` list contains the decimal values of the Roman numerals, and the `syb` list contains the corresponding Roman numerals.

The function initializes an empty string `roman_num` to store the Roman numeral. It then iterates through the `val` list, subtracting the current value from the input number as many times as possible, and appending the corresponding Roman numeral to `roman_num` each time.

The function returns the Roman numeral as a lowercase string.

The function works for integers between 1 and 1000. For larger integers, the function would need to be modified to handle the additional Roman numerals. For smaller integers, the function would need to be modified to handle the additional Roman numerals and to handle the subtraction of smaller values from the input number.