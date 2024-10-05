
Here's a Python function that calculates 2^n modulo p:

```python
def modp(n, p):
    # Using the binary exponentiation method
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * 2) % p
        n = n // 2
        p = p ** 2 % p
    return result
```

This function uses binary exponentiation to calculate the result in O(log n) time.

The function takes two parameters, n and p. n is the exponent and p is the modulus.

The function first initializes the result variable to 1. Then, it enters a while loop that continues until n becomes zero. Inside the loop, it checks if the last bit of n is 1. If so, it multiplies the result by 2 and reduces the result modulo p. Then, it divides n by 2 and squares p modulo p. This process continues until n becomes zero.

Finally, the function returns the result, which is the value of 2^n modulo p.

You can test the function with the provided test cases to verify its correctness.

```python
print(modp(3, 5))  # Expected output: 3
print(modp(1101, 101))  # Expected output: 2
print(modp(0, 101))  # Expected output: 1
print(modp(3, 11))  # Expected output: 8
print(modp(100, 101))  # Expected output: 1
```

These test cases cover different scenarios, including edge cases like n = 0, to ensure the function works correctly.

Note: The provided code is in Python, but the algorithm can be implemented in any programming language that supports bitwise operations and modular arithmetic.

```python
```

In Python, the bitwise operations are supported by the bitwise operators such as bitwise AND (&), bitwise OR (|), bitwise XOR (^), left shift (<<), and right shift (>>). These operations can be used to extract the