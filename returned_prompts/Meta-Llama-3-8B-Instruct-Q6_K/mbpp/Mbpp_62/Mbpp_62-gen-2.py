```
def smallest_num(lst):
    return min(lst)
```
The `min()` function in Python returns the smallest item in an iterable or the smallest of two or more arguments. It works with lists, tuples, dictionaries, sets, and strings. If the iterable is empty, it raises a ValueError. In this case, we use it to find the smallest number in the list.  The unit test `assert smallest_num([10, 20, 1, 45, 99]) == 1` confirms that the function works correctly.  



