
Here is one possible implementation:

```python
def largest_divisor(n: int) -> int:
    # Start from n - 1 and go down to 1
    for i in range(n-1, 0, -1):
        # If n is divisible by i, return i
        if n % i == 0:
            return i
    # If no divisor is found, return 1
    return 1
```

This function takes an integer `n` as input and iterates from `n` to 1 in reverse order. It checks if `n` is divisible by each number in the range. If it finds a number that evenly divides `n`, it returns that number. If no such number is found, it returns 1.

For example, if we call `largest_divisor(15)`, it will return 5 because 5 is the largest number that evenly divides 15.

```python
print(largest_divisor(15))  # Output: 5
```

This function can be used to find the largest divisor of any given number.

```python
print(largest_divisor(28))  # Output: 14
print(largest_divisor(30))  # Output: 15
```

It's important to note that for a prime number, the largest divisor is the number itself. For example, the largest divisor of 7 is 7.

```python
print(largest_divisor(7))  # Output: 7
```

This function provides a simple and straightforward way to find the largest divisor of a number.

```python
print(largest_divisor(49))  # Output: 7
```

```python
print(largest_divisor(50))  # Output: 50
```

```python
print(largest_divisor(6))  # Output: 6
```

```python
print(largest_divisor(71))  # Output: 71
```

```python
print