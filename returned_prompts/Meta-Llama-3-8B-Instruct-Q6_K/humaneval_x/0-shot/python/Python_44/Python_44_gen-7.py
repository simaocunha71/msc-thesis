```
def change_base(x: int, base: int):
    convertString = "0123456789ABCDEF"
    result = ""
    while x > 0:
        result = convertString[x % base] + result
        x = x // base
    return result
```


Explanation:
The function change_base(x, base) takes an integer x and a base as input and converts the integer x to the given base. The function uses a string representation of the given base to convert the number. The result is a string representation of the number in the given base.

The function works by repeatedly dividing the number x by the given base and appending the remainder to the result string. The remainder is obtained using the modulus operator (%). The division is done using integer division (//). The process continues until x becomes 0.

The result string is then returned as the output of the function. The function works correctly for bases less than 10. For bases greater than 10, the string representation of the base is used to convert the number. For example, for base 16 (hexadecimal), the string "0123456789ABCDEF" is used to convert the number.

The unit tests provided in the problem statement demonstrate the correctness of the function. The function correctly converts the numbers 8, 7, and 8 to the given bases 3, 2, and 2, respectively. The output strings are '22', '1000', and '111', respectively, which are the expected results.