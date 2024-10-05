Here is the solution:

```python
def change_base(x: int, base: int):
    convertString = "0123456789ABCDEF"
    if x < base:
        return convertString[x]
    else:
        return change_base(x//base, base) + convertString[x%base]
```

Explanation:
The function `change_base` converts an integer `x` to a base `base` numeral system. The base is assumed to be less than 10. The function uses recursion to achieve this. 

The base conversion is done by repeatedly dividing the number by the base and appending the remainder to the result. The remainder is obtained using the modulus operator `%`. 

The remainder is then looked up in the `convertString` to get the corresponding digit in the new base. This process is repeated until the number is reduced to 0. 

Finally, the function returns the converted string. 

For example, when `x` is 8 and `base` is 3, the function will convert 8 to 22 in base 3. When `x` is 8 and `base` is 2, the function will convert 8 to 1000 in base 2. When `x` is 7 and `base` is 2, the function will convert 7 to 111 in base 2. 

The unit tests provided in the problem ensure that the function works correctly for these examples. 

This function can be used to convert numbers to any base less than 10. It is a simple and efficient way to achieve this. 