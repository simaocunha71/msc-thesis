```
def power_base_sum(base, power):
    result = base ** power
    return sum(int(digit) for digit in str(result))
```
The function `power_base_sum` takes two arguments, `base` and `power`. It calculates the value of `base` to the power of `power` using the exponentiation operator `**`. This result is then converted to a string using the `str` function. The `sum` function is used to calculate the sum of all the digits in the string. The `int` function is used to convert each character in the string back to an integer before summing. This is a common approach to solve this problem. The unit test `assert power_base_sum(2,100)==115` checks that the function works correctly. 