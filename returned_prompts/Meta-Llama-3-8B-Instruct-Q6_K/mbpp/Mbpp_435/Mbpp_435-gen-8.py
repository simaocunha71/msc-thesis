```
def last_Digit(n):
    return n % 10
```


This function works by using the modulus operator `%` which returns the remainder of the division of `n` by `10`. The last digit of a number is the remainder when divided by `10`. For example, `123 % 10` gives `3` and `456 % 10` gives `6`. The unit test `assert last_Digit(123) == 3` confirms this. The function returns this remainder as the last digit of the given number.  



Here is the output of the function for the given test case:

```
print(last_Digit(123))
Output: 3
```



This function works correctly for all positive integers as input. It does not handle negative numbers or non-integer inputs. If you need to handle these cases, you would need to add additional code to the function. For example, you could take the absolute value of the input to ensure it is positive, or check if the input is an integer before trying to calculate its last digit.  



Here is an example of how you might modify the function to handle negative numbers:

```
def last_Digit(n):
    return abs(n) % 10
```


This version of the function uses the built-in `abs` function to take the absolute value of the input before calculating its last digit. This means it will work correctly for negative inputs, returning the same result as the original function would for the corresponding positive input.  



For example, `last_Digit(-123)` would return `3`, the same as `last_Digit(123)`.  



However, it's worth noting that this function still does not handle non-integer inputs. If you need to handle these cases, you would need to add additional code to check if the input is an integer before trying to calculate its last digit.  



For example, you could use a try-except block to catch the `TypeError` that would be raised if the input is not an integer:

```
def last_Digit(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    return abs(n) % 10
```


This version of the function checks if the input is an integer using the `isinstance` function. If it is not an integer, it raises a `TypeError` with a message indicating that the input must be an integer. If the input is an integer, it calculates its last