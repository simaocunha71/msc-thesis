Here's one way to do it:

```python
def sum_negativenum(nums):
    # Initialize an empty list to store the negative numbers
    negative_nums = []
    # Traverse through the given list of numbers
    for num in nums:
        # If the number is negative, add it to the list
        if num < 0:
            negative_nums.append(num)
    # Return the sum of the negative numbers
    return sum(negative_nums)
```

You can test the function with the provided assert statement:

```python
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
```

This will return True if the function correctly calculates the sum of the negative numbers, and False otherwise.

```python
def sum_negativenum(nums):
    # Initialize an empty list to store the negative numbers
    negative_nums = []
    # Traverse through the given list of numbers
    for num in nums:
        # If the number is negative, add it to the list
        if num < 0:
            negative_nums.append(num)
    # Return the sum of the negative numbers
    return sum(negative_nums)
```

You can test the function with the provided assert statement:

```python
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
```
This will return True if the function correctly calculates the sum of the negative numbers, and False otherwise.

```python
def sum_negativenum(nums):
    # Initialize an empty list to store the negative numbers
    negative_nums = []
    # Traverse through the given list of numbers
    for num in nums:
        # If the number is negative, add it to the list
        if num < 0:
            negative_nums.append(num)
    # Return the sum of the negative numbers
    return sum(negative_