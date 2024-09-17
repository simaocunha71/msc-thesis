```
def check_greater(arr, num):
    return all(num > i for i in arr)
```
The function `check_greater` takes two parameters: `arr` (a list of numbers) and `num` (the number to be checked). It returns `True` if `num` is greater than all elements in `arr`, and `False` otherwise.

The unit test `assert check_greater([1, 2, 3, 4, 5], 4) == False` indicates that the function should return `False` when `num` is 4, which is not greater than all elements in the array `[1, 2, 3, 4, 5]`.

The function uses the `all` function and a generator expression to check if `num` is greater than all elements in `arr`. The `all` function returns `True` if all elements in the iterable (in this case, the generator expression) are true. The generator expression `num > i for i in arr` yields `True` for each element `i` in `arr` if `num` is greater than `i`, and `False` otherwise. If any element in `arr` is greater than or equal to `num`, the `all` function will return `False`. If all elements in `arr` are less than `num`, the `all` function will return `True`. 





```
```python
def check_greater(arr, num):
    return all(num > i for i in arr)
```
This function checks if a given number `num` is greater than all elements in the array `arr`. It returns `True` if `num` is greater than all elements in `arr`, and `False` otherwise.

Here's how you can use this function:

```
arr = [1, 2, 3, 4, 5]
num = 6
print(check_greater(arr, num))  # Output: True

arr = [1, 2, 3, 4, 5]
num = 4
print(check_greater(arr, num))  # Output: False
```

In the first example, `num` (6) is greater than all elements in `arr`, so the function returns `True`. In the second example, `num` (4) is not greater than all elements in `arr`, so the function returns `False`.