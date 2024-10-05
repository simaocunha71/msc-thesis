```
def is_sorted(lst):
    if len(set(lst)) != len(lst):
        return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```



Here is an explanation of the code:

1. `if len(set(lst)) != len(lst):` This line checks if there are any duplicate numbers in the list. If there are, it returns `False`. The `set` function is used to create a set from the list, which removes duplicates. If the length of the set is not equal to the length of the list, then there were duplicates.

2. `return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))` This line checks if the list is sorted in ascending order. The `all` function is used to check if all elements in an iterable (in this case, a generator expression) are true. The generator expression `lst[i] <= lst[i+1] for i in range(len(lst)-1)` checks if each element in the list is less than or equal to the next one. If any element is not less than or equal to the next one, the function will return `False`. If all elements are less than or equal to the next one, the function will return `True`. The `-1` in `range(len(lst)-1)` is used to avoid an `IndexError` when checking the last element in the list.