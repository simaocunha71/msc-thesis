The solution to this problem is:

```python
def change_base(x: int, base: int):
    convertString = "0123456789ABCDEF"
    result = ""
    
    while x > 0:
        result = convertString[x % base] + result
        x = x // base
    
    return result
```


The `change_base` function takes two integer arguments, `x` and `base`. It converts the integer `x` to a base `base` and returns the result as a string. The base `base` is assumed to be less than 10.

The function uses a while loop to repeatedly divide the integer `x` by the base `base` and prepend the remainder to the result string. The remainder is obtained using the modulus operator `%`. The integer division is performed using the floor division operator `//`.

The convertString is used to convert the remainder to the corresponding character in the target base. This is done by indexing into the convertString with the remainder.

Finally, the function returns the result string.

The unit tests provided ensure that the function works correctly for different inputs. For example, `change_base(8, 3)` returns `'22'`, which is the decimal representation of the octal number `8` converted to base `3`. Similarly, `change_base(8, 2)` returns `'1000'`, which is the decimal representation of the binary number `8` converted to base `2`. The test `change_base(7, 2)` returns `'111'`, which is the decimal representation of the binary number `7` converted to base `2`.