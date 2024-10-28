```
def second_smallest(lst):
    if len(lst) < 2:
        return None
    lst.sort()
    return lst[1]
```
This function sorts the list in ascending order and returns the second element, which is the second smallest number. If the list has less than two elements, it returns None.

The unit test `assert second_smallest([1, 2, -8, -2, 0, -2])==-2` ensures that the function works correctly. It checks that the function returns -2, which is the second smallest number in the list.