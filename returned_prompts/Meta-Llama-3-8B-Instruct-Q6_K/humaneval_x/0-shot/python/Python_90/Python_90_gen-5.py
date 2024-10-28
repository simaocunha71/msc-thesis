```
def next_smallest(lst):
    if not lst:
        return None
    unique_lst = list(set(lst))
    unique_lst.sort()
    if len(unique_lst) < 2:
        return None
    return unique_lst[1]
```


This function first checks if the input list is empty. If it is, the function returns None. Then, it converts the list to a set (which removes any duplicates) and converts it back to a list. It then sorts this list. If the length of the sorted list is less than 2, the function returns None (because there is no 2nd smallest element). Otherwise, it returns the second element of the sorted list, which is the 2nd smallest element in the original list.