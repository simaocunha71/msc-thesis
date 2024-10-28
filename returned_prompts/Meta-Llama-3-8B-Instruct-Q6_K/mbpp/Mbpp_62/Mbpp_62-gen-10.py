```
def smallest_num(lst):
    return min(lst)
```
This function uses the built-in `min()` function in Python, which returns the smallest item in an iterable or the smallest of two or more arguments. It works with lists, tuples, dictionaries, sets, and strings. If the list is empty, it will raise a ValueError. If you want to handle the empty list case, you can add a simple check:
```
def smallest_num(lst):
    if not lst:
        return None  # or any other default value
    return min(lst)
```


In this problem, the unit test `assert smallest_num([10, 20, 1, 45, 99]) == 1` suggests that the function should find the smallest number in the list. The `min()` function is a natural fit for this task, as it returns the smallest item in an iterable. The function takes a list as an argument and returns the smallest number in the list. If the list is empty, the function will raise a ValueError. You can add a check to handle this case if you want to return a default value instead.