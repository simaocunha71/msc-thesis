```
def int_to_mini_roman(number):
    roman_numerals = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd',
        100: 'c', 90: 'xc', 50: 'l', 40: 'xl',
        10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'
    }
    result = ''
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value
    return result.lower()
```


This function converts an integer from 1 to 1000 to its roman numeral equivalent in lowercase. It does this by using a dictionary to map the decimal values to their corresponding roman numerals. It then iterates over the dictionary in descending order, subtracting the decimal value from the input number as many times as possible and appending the corresponding roman numeral to the result. The function returns the result as a string in lowercase. The `sorted` function is used with the `reverse=True` argument to iterate over the dictionary in descending order of the decimal values. This ensures that the largest possible roman numeral is used first, which is necessary for correct conversion. The `while` loop is used to subtract the decimal value from the input number as many times as possible and append the corresponding roman numeral to the result. This ensures that the roman numeral is represented correctly, even if the input number is not a perfect multiple of the decimal value. For example, the roman numeral for 4 is 'iv', not 'iiiii'. The `return` statement is used to return the result as a string in lowercase. This ensures that the roman numeral is returned in the correct case, which is lowercase according to the problem statement. The function is tested with the examples provided in the problem statement, and it returns the correct results for these examples. Therefore, the function is correct and can be used to convert integers from 1 to 1000 to their roman numeral equivalents in lowercase.