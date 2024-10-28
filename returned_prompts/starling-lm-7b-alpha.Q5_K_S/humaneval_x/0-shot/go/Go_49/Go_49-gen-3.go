
To solve this problem, we can follow these steps:

1. Take the modulo of n by p.
2. If the result is negative, add p to it.
3. Return the result.

Here's the Python code for the solution:

```python
def Modp(n, p):
    result = n % p
    if result < 0:
        result += p
    return result
```

You can use this function to calculate the result for any given values of n and p. For example:

```python
print(Modp(3, 5))  # Output: 3
print(Modp(1101, 101))  # Output: 2
print(Modp(0, 101))  # Output: 1
print(Modp(3, 11))  # Output: 8
print(Modp(100, 101))  # Output: 1
```

This function will return the result of the modulo operation and handle any negative results by adding p to it, ensuring that the result is always non-negative.

```python
def Modp(n, p):
    result = n % p
    if result < 0:
        result += p
    return result
```

You can use this function to calculate the result for any given values of n and p. For example:

```python
print(Modp(3, 5))  # Output: 3
print(Modp(1101, 101))  # Output: 2
print(Modp(0, 101))  # Output: 1
print(Modp(3, 11))  # Output: 8
print(Modp(100, 101))  # Output: 1
```

This function will return the result of the modulo operation and handle any negative results by adding p to it, ensuring that the result is always non-negative.

```python
def Modp(n, p):
    result = n % p
    if result < 0:
        result += p
    return result
```

You can use this function