```
def is_sorted(lst):
    if len(lst) <= 1:
        return True
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    if len(set(lst)) != len(lst):
        return False
    return True
```


Explanation:
The function `is_sorted` takes a list of integers as input and returns a boolean value indicating whether the list is sorted in ascending order.

First, it checks if the list has less than or equal to one element. If so, it returns `True` because a list with one or zero elements is considered sorted.

Then, it iterates through the list and checks if each element is less than or equal to the next one. If it finds an element that is greater than the next one, it immediately returns `False`, indicating that the list is not sorted.

Next, it checks if the list has any duplicates by converting the list to a set (which removes duplicates) and comparing the length of the set to the length of the original list. If the lengths are different, it means the list had duplicates, so it returns `False`.

If the function hasn't returned `False` by this point, it means the list is sorted and has no duplicates, so it returns `True`.