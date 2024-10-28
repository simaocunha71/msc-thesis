```
def next_power_of_2(n):
    if n <= 0:
        return 1
    return 2 ** (n - 1).bit_length()
```


This function works by first checking if `n` is less than or equal to 0. If it is, the function returns 1, as the smallest power of 2 greater than or equal to 0 is 1.

If `n` is greater than 0, the function uses the `bit_length` method of the integer `n - 1` to find the number of bits needed to represent `n - 1` in binary. This is because the smallest power of 2 greater than or equal to `n` will be the next power of 2 with `n - 1` bits.

The `bit_length` method returns the number of bits necessary to represent an integer, which is equivalent to the number of times the integer needs to be right-shifted to become 0.

The function then raises 2 to the power of the number of bits found using the `bit_length` method, which gives the smallest power of 2 greater than or equal to `n`.

This function works correctly because the smallest power of 2 greater than or equal to `n` will always be the next power of 2 with `n - 1` bits. For example, the smallest power of 2 greater than or equal to 5 is 8, which has 3 bits (100 in binary), and the smallest power of 2 greater than or equal to 8 is 16, which has 4 bits (10000 in binary). This function correctly returns these values.