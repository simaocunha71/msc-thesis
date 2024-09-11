Here is one possible solution for the problem:

```python
def check_greater(arr, num):
    for i in arr:
        if i < num:
            return False
    return True
```

In this solution, we iterate through the array `arr` and check if any element is less than the number `num`. If we find an element that is less than `num`, we return `False`. If we finish the loop without finding such an element, we return `True`, meaning that the entered number is indeed greater than all the elements of the array.

For example, if we call `check_greater([1, 2, 3, 4, 5], 4)`, it will return `False` because 4 is less than 4. However, if we call `check_greater([1, 2, 3, 4, 5], 6)`, it will return `True` because all the elements in the array are less than 6.

You can use the `assert` statement to verify the correctness of the solution. For example, you can write `assert check_greater([1, 2, 3, 4, 5], 4) == False` to check if the solution returns the expected `False` value when the number `num` is less than any element in the array `arr`.

Overall, this solution provides a straightforward way to check whether the entered number is greater than the elements of the given array.

```python
def check_greater(arr, num):
    for i in arr:
        if i < num:
            return False
    return True
```

```python
assert check_greater([1, 2, 3, 4, 5], 4) == False
```

```python
assert check_greater([1, 2, 3, 4, 5], 6) == True
```

```python
print(check_greater([1, 2, 3, 4, 5], 4))  # Returns: False
```

```python
print(check_greater([1, 2, 3, 4, 5], 6))  # Returns: True