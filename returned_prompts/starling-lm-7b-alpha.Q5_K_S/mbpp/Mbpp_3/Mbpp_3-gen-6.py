Here is a Python function to identify non-prime numbers:

```python
def is_not_prime(n):
    if n <= 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False
```

To use this function, you can call it with a number and it will return `True` if the number is not prime and `False` if it is prime. For example, to check if 2 is not prime, you can call the function as follows:

```python
result = is_not_prime(2)
print(result)  # This will print: True
```

In this code, the function `is_not_prime` first checks if the number `n` is less than or equal to 1. If it is, the function returns `True`, indicating that the number is not prime. Next, the function uses a `for` loop to iterate from 2 to the square root of `n` (inclusive). It checks if `n` is divisible by any number in this range. If it is, the function returns `True`, indicating that the number is not prime. If the loop completes without finding a factor, the function returns `False`, indicating that the number is prime.

It's important to note that this implementation is not the most efficient way to determine if a number is prime. There are faster algorithms available, such as the Miller-Rabin primality test or the AKS primality test. However, this simple implementation should be sufficient for most purposes.

Here's a demonstration of how you can use this function:

```python
def test_is_not_prime():
    assert is_not_prime(2) == False
    assert is_not_prime(3) == False
    assert is_not_prime(4) == True
    assert is_not_prime(5) == False
    assert is_not_prime(6) == True
    assert is_not_prime(7) == False
    assert is_not_prime(8) == True
    assert is_not_prime(9) == True
    assert is_not_prime(10)