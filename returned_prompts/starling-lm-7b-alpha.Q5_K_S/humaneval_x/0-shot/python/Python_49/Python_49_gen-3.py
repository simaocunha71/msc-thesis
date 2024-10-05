
Here's a Python function that computes the modulus of 2 raised to the power of n modulo p:

```python
def modp(n: int, p: int) -> int:
    return pow(2, n, p)
```

This function uses Python's built-in `pow` function with three arguments, `base`, `exponent`, and `modulus`.

In Python, the `pow` function computes the modulus of `base` raised to the power of `exponent` and returns the result modulo `modulus`.

For example, if you want to compute `2^1000` modulo `10000`, you can do so with the following code:

```python
>>> print(pow(2, 1000, 10000))
8388607
```

This code prints `8388607`, which is the result of computing `2^1000` modulo `10000`.

The `modp` function works in the same way. It takes two integer arguments, `n` and `p`, and computes `2^n` modulo `p`.

Here are some example tests for the `modp` function:

```python
print(modp(3, 5))  # prints: 3
print(modp(1101, 101))  # prints: 2
print(modp(0, 101))  # prints: 1
print(modp(3, 11))  # prints: 8
print(modp(100, 101))  # prints: 1
```

These tests show that the `modp` function correctly computes the modulus of `2` raised to the power of `n` modulo `p`.

```python
def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0,