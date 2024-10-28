```
def next_power_of_2(n):
    if n == 0:
        return 1
    else:
        return 2**(n-1).bit_length()
```
The function `next_power_of_2(n)` finds the smallest power of 2 greater than or equal to `n`. 

If `n` is 0, the function returns 1, because the smallest power of 2 greater than 0 is 2^1, which is 2.

If `n` is not 0, the function uses the `bit_length()` method of the integer `2**(n-1)` to find the number of bits required to represent `2**(n-1)`. This is because `2**(n-1)` is the largest power of 2 less than `n`, so `2**(n-1)` has `n-1` bits. Therefore, the smallest power of 2 greater than `n-1` is `2**((n-1).bit_length())`, which is the function's return value. 

The `bit_length()` method returns the number of bits necessary to represent an integer, excluding the sign and leading zeros. For example, `10.bit_length()` returns 3, because 10 can be represented with 3 bits (101 in binary). 

The unit test `assert next_power_of_2(0) == 1` ensures that the function returns 1 when `n` is 0. This is because the smallest power of 2 greater than 0 is 2^1, which is 2. However, the function is designed to return 1 when `n` is 0, so this test passes. 

This function works correctly for all non-negative integers `n`. For negative integers `n`, the function will return the smallest power of 2 greater than or equal to the absolute value of `n`, which may not be what the problem intends. To handle negative integers correctly, the function could be modified to return the smallest power of 2 greater than or equal to the absolute value of `n`, and then return the result with the same sign as `n`. However, this is not necessary for the given unit test. 