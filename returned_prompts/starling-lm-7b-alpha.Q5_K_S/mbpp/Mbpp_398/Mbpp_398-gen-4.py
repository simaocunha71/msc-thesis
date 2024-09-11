def sum_of_digits(nums):
    """
    Sums the digits of each number in a given list
    """
    total = 0
    for num in nums:
        while num:
            total += num % 10
            num = num // 10
    return total

sum_of_digits([10,2,56])#14

# Test Cases
assert sum_of_digits([10,2,56])==14
assert sum_of_digits([345, 12, 32])==10

#print(sum_of_digits([345, 12, 32]))




```

```
"""
Write a function to compute the sum of digits of each number of a given list.

Test Cases:
assert sum_of_digits([10,2,56])==14
assert sum_of_digits([345, 12, 32])==10
"""

def sum_of_digits(nums):
    """
    Sums the digits of each number in a given list
    """
    total = 0
    for num in nums:
        while num:
            total += num % 10
            num = num // 10
    return total
```

```
"""
Write a function to compute the sum of digits of each number of a given list.

Test Cases:
assert sum_of_digits([10,2,56])==14
assert sum_of_digits([345, 12, 32])==10
"""

def sum_of_digits(nums):
    """
    Sums the digits of each number in a given list
    """
    total = 0
    for num in nums:
        while num:
            total += num % 10
            num = num // 10
    return total
```

```python
"""
Write a function to compute the sum of digits of each number of a given list.

Test Cases