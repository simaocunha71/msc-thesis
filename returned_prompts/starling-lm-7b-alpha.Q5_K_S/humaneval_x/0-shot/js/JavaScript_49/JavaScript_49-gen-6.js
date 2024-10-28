To calculate 2^n modulo p, we can use the following steps:

1. Initialize a variable `result` to 1.
2. While `n` is greater than 0, perform the following steps:
   a. Multiply `result` by 2.
   b. If the least significant bit of `n` is 1, add `p` to `result`.
   c. Right shift `n` by 1.
3. Return the value of `result`.

Here's an implementation of the `modp` function:

```python
def modp(n, p):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n = n >> 1
    return result
```

You can test the function with the provided examples:

```python
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

In the `modp` function, we initialize the `result` variable to 1. Then, in the while loop, we multiply the `result` by 2 and add `p` to it if the least significant bit of `n` is 1. We right shift `n` by 1 in each iteration to extract the next bit. Finally, we return the value of `result`.

Using this approach, we can efficiently calculate 2^n modulo p, taking into account the numerics involved.

*/
def modp(n, p):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n = n >> 1
    return result

# Test cases
print(modp(3, 5))  # Output: 3
print(modp(11