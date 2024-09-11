```python
def first_odd(lst):
    for item in lst:
        if item % 2 != 0:
            return item
```

Explanation:
This function will return the first odd number in the list. It will go through each item in the list and check if the item is odd (not divisible by 2). If an odd item is found, it will return that item and stop the function. If no odd item is found, the function will return None.

```python
# Test the function
print(first_odd([1,3,5]))  # Output: 1
print(first_odd([1,2,3,4,5]))  # Output: 1
print(first_odd([2,4,6]))  # Output: None
```

This is a simple function that will work for most cases. However, it's worth noting that if all the numbers in the list are even, the function will return None.

This function will work with any input list of numbers, regardless of the size or the values of the numbers.

It's also worth noting that this function is not optimized for speed or memory usage. It's a straightforward solution that will work, but there are more efficient ways to solve this problem if speed or memory usage is a concern.
```

```

```python
def first_odd(lst):
    for item in lst:
        if item % 2 != 0:
            return item
```

Explanation:
This function will return the first odd number in the list. It will go through each item in the list and check if the item is odd (not divisible by 2). If an odd item is found, it will return that item and stop the function. If no odd item is found, the function will return None.

```python
# Test the function
print(first_odd([1,3,5]))  # Output: 1
print(first_odd([1,2,3,4,5]))  # Output: 1
print(first_odd([2,4,6]))  # Output: None
```

This is a simple function that will work for most cases. However, it's worth noting that if all the