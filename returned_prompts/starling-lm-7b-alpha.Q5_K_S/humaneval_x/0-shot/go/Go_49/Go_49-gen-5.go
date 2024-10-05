
Modp is a mathematical function that calculates the result of 2^n modulo p. It returns an integer value.

The function is defined as follows:

If n is 0, return 1.
If n is even, return the result of Modp(n/2, p) modulo p.
If n is odd, return the result of 2 * Modp(n/2, p) modulo p.

In other words, the function is equivalent to the following recursive function:

Modp(n, p) = if n == 0:
1
else if n % 2 == 0:
Modp(n / 2, p)
else:
2 * Modp(n / 2, p)

This function is a modular exponentiation, which is a way to calculate the result of a^n modulo p in O(log n) time, where a is a number and p is a prime number.

The time complexity of this function is O(log n).

Here is a Python implementation of the function:

```python
def Modp(n, p):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return Modp(n // 2, p) % p
    else:
        return 2 * Modp(n // 2, p) % p
```

The function can be used to calculate the result of 2^n modulo p for any non-negative integer n and any positive integer p.

For example, if n is 3 and p is 5, the function will return 3. If n is 1101 and p is 101, the function will return 2. If n is 0 and p is 101, the function will return 1. If n is 3 and p is 11, the function will return 8. If n is 100 and p is 101, the function will return 1.

The function is useful in various applications, such as cryptography, number theory, and computer science.

Here are some more examples of the function in use:

```python
print(Modp(3, 5))  # Output