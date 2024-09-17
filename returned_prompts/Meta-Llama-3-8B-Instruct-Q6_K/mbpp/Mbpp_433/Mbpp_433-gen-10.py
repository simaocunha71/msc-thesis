```
def check_greater(arr, num):
    return all(num > x for x in arr)
```



The function `check_greater` takes two parameters: an array `arr` and a number `num`. It returns `True` if `num` is greater than all elements in the array, and `False` otherwise.

The unit test `assert check_greater([1, 2, 3, 4, 5], 4) == False` suggests that the function should return `False` when the input number `num` is not greater than all elements in the array. Therefore, the function is implemented using the `all` function, which returns `True` if all elements in the iterable (in this case, the array) are true. The iterable is a generator expression that checks if `num` is greater than each element in the array. If `num` is not greater than any element in the array, the function returns `False`. Otherwise, it returns `True`.