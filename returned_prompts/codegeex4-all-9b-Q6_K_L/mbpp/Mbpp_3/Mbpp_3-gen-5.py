```python
def is_not_prime(n):
    if n <= 1:
        return True
    if n == 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

assert is_not_prime(2) == False
```