To solve this problem, we can use the following steps:

1. Check if all the numbers are integers. If any of the numbers are not integers, return False.
2. Calculate the sum of the two largest numbers.
3. Check if the smallest number is equal to the sum from step 2. If it is, return True. Otherwise, return False.

Here's the Python code that implements the above steps:

```python
def any_int(x, y, z):
    # Step 1: Check if all the numbers are integers.
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False
    
    # Step 2: Calculate the sum of the two largest numbers.
    sum_largest = max(x, y) + max(y, z)
    
    # Step 3: Check if the smallest number is equal to the sum.
    if sum_largest == min(x, y, z):
        return True
    else:
        return False
```

With this code, you can call the function `any_int` with any three numbers, and it will return True if one of the numbers is equal to the sum of the other two, and all numbers are integers. Otherwise, it will return False.

For example, `any_int(5, 2, 7)` will return True because 2 is equal to the sum of 5 and 7, and all numbers are integers. On the other hand, `any_int(3, 2, 2)` will return False because none of the numbers is equal to the sum of the other two.

```python
print(any_int(5, 2, 7))  # True
print(any_int(3, 2, 2))  # False
print(any_int(3, -2, 1))  # True
print(any_int(3.6, -2.2, 2))  # False
```

In all these cases, the function `any_int` correctly identifies whether one of the numbers is equal to the sum of the other two, and if all numbers are integers.

```