```python
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return 2 * (10 ** (n - 1) - 1)

print(starts_one_ends(1))  # 2
print(starts_one_ends(2))  # 18
print(starts_one_ends(3))  # 180
```