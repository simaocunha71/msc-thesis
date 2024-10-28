
In order to calculate the value of 2^n modulo p, we can use the following steps:

1. Initialize a variable result with the value of 1.
2. Initialize a variable exponent with the value of n.
3. Initialize a variable modulus with the value of p.
4. While exponent is not equal to 0:
   a. Multiply result by 2.
   b. Divide result by modulus.
   c. Subtract 1 from exponent.
5. Return the final result.

Here's the Python code that implements the above algorithm:

```python
def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics)."""
    result = 1
    exponent = n
    modulus = p
    while exponent != 0:
        result *= 2
        result %= modulus
        exponent -= 1
    return result
```

You can test the function using the provided test cases:

```python
print(modp(3, 5))  # Output: 3
print(modp(1101, 101))  # Output: 2
print(modp(0, 101))  # Output: 1
print(modp(3, 11))  # Output: 8
print(modp(100, 101))  # Output: 1
```

The function `modp` takes two arguments: `n` and `p`. It calculates the value of `2^n mod p` using a while loop. The while loop runs until the exponent becomes 0. Inside the loop, the result is multiplied by 2 and then divided by the modulus. The exponent is decremented by 1 in each iteration. Finally, the function returns the calculated result.

This implementation ensures that the result is always less than the modulus, preventing overflow and maintaining accuracy.

It's important to note that this implementation assumes that the input values are non-negative integers. If negative values are allowed, additional checks should be added to handle them appropriately.

Additionally, it's worth mentioning that for large values of `n`, the result