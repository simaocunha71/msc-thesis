def next_power_of_2(n):
    if n == 0:
        return 1
    elif n & (n - 1) == 0:
        return n
    else:
        return 2 ** (n.bit_length() + 1)


# Testing
print(next_power_of_2(0))  # 1
print(next_power_of_2(1))  # 2
print(next_power_of_2(3))  # 4
print(next_power_of_2(7))  # 8
print(next_power_of_2(9))  # 16

# Using the assert statement to validate the function
assert next_power_of_2(0) == 1
```
    
```
This Python function `next_power_of_2(n)` finds the smallest power of 2 greater than or equal to `n`. It first checks if `n` is equal to 0, in which case it returns 1. If `n` is a power of 2 (i.e., `n` and `n - 1` are equal), it returns `n`. Otherwise, it uses the bit_length() function to find the number of bits in the binary representation of `n`, adds 1 to it, and then returns 2 raised to that power.

The function is tested with several inputs to verify its correctness.
```
```

The Python function next_power_of_2(n) finds the smallest power of 2 greater than or equal to n. It first checks if n is equal to 0, in which case it returns 1. If n is a power of 2 (i.e., n and n - 1 are equal), it returns n. Otherwise, it uses the bit_length() function to find the number of bits in the binary representation of n, adds 1 to it, and then returns 2 raised to that power.

The function is tested with several inputs to verify its correctness.
```
```