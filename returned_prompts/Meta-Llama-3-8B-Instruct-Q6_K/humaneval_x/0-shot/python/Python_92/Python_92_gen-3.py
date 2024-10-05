```
def any_int(x, y, z):
    if not all(isinstance(i, int) for i in [x, y, z]):
        return False
    if x == y + z or x == z + y or y == x + z or y == z + x or z == x + y or z == y + x:
        return True
    return False
```


The function `any_int(x, y, z)` checks if one of the numbers is equal to the sum of the other two. It first checks if all inputs are integers using the `isinstance` function in a list comprehension. If any of the inputs are not integers, it immediately returns `False`. If all inputs are integers, it then checks if one of the numbers is equal to the sum of the other two using multiple if statements. If it finds a match, it returns `True`. If it doesn't find a match after checking all the possible combinations, it returns `False`. 

This function works for both positive and negative integers, and also handles cases where the sum of two numbers is equal to the third number. For example, `any_int(3, -2, 1)` returns `True` because `3` is equal to the sum of `-2` and `1`. 

The function also correctly handles cases where the inputs are not integers. For example, `any_int(3.6, -2.2, 2)` returns `False` because `3.6` is not an integer. 





Test cases:

```
print(any_int(5, 2, 7))  # ➞ True
print(any_int(3, 2, 2))  # ➞ False
print(any_int(3, -2, 1))  # ➞ True
print(any_int(3.6, -2.2, 2))  # ➞ False
``` 





Output:

```
True
False
True
False
``` 





This function passes all the test cases. 