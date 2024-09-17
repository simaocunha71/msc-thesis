```
def check_greater(arr, num):
    return all(num > x for x in arr)
```
The function `check_greater` takes two parameters: an array `arr` and a number `num`. It returns a boolean value indicating whether `num` is greater than all elements in the array.

The unit test `assert check_greater([1, 2, 3, 4, 5], 4) == False` suggests that the function should return `False` when `num` is not greater than all elements in the array, which is the case when `num` is 4 and the array is [1, 2, 3, 4, 5].

The function uses the `all` function with a generator expression to check if `num` is greater than all elements in the array. The `all` function returns `True` if all elements of the iterable are true. In this case, the iterable is the generator expression `num > x for x in arr`, which generates a sequence of boolean values indicating whether `num` is greater than each element in the array. If any of these values are `False`, the `all` function returns `False`, indicating that `num` is not greater than all elements in the array. If all values are `True`, the `all` function returns `True`, indicating that `num` is greater than all elements in the array.