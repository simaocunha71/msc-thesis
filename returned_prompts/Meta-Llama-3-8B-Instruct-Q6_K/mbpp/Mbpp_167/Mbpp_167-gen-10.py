```
def next_power_of_2(n):
    if n == 0:
        return 1
    else:
        return 2 ** (n - 1).bit_length()
```


This function works by first checking if the input number is 0. If it is, the function returns 1, because the smallest power of 2 greater than or equal to 0 is 1. If the input number is not 0, the function uses the `bit_length` method of the `int` type, which returns the number of bits necessary to represent the number in binary. It then subtracts 1 from this value and uses it as the exponent in a `2 **` operation to find the smallest power of 2 greater than or equal to the input number.

For example, if the input number is 8, the function will return `2 ** 3`, which is 8. If the input number is 15, the function will return `2 ** 4`, which is 16. If the input number is 0, the function will return 1, as expected. This function is efficient and works correctly for all positive integers.