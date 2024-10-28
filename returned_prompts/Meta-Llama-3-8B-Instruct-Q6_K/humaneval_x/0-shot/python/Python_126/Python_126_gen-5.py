```
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return len(set(lst)) == len(lst)
```
This function works by iterating over the list and checking if each element is less than or equal to the next one. If it finds a pair of elements that are not in order, it immediately returns `False`. If it gets through the entire list without finding any out-of-order pairs, it checks if the length of the set of unique elements in the list is equal to the length of the list itself. If it is, then the list is sorted and has no duplicates, so it returns `True`. Otherwise, it returns `False`.