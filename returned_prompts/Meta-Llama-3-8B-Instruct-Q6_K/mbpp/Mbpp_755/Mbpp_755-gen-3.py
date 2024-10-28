```
def second_smallest(lst):
    if len(lst) < 2:
        return None
    lst.sort()
    return lst[1]
```
This function first checks if the list has less than 2 elements. If it does, it returns None. Otherwise, it sorts the list in ascending order and returns the second element, which is the second smallest number in the list.

The unit test `assert second_smallest([1, 2, -8, -2, 0, -2])==-2` helps to clarify that the function should return the second smallest number in the list, even if it appears multiple times. For example, in the list `[1, 2, -8, -2, 0, -2]`, the number `-2` appears three times, but it is still the second smallest number. The function should return `-2` in this case.