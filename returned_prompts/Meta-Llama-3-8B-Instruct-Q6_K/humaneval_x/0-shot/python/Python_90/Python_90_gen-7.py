```
def next_smallest(lst):
    if len(lst) < 2:
        return None
    sorted_lst = sorted(set(lst))
    if len(sorted_lst) < 2:
        return None
    return sorted_lst[1]
```
The function first checks if the list is empty or has only one element. If so, it returns None. Then, it removes duplicates by converting the list to a set and sorting the set. If the length of the sorted set is less than 2, it means the list has only one unique element, so the function returns None. Otherwise, it returns the second element of the sorted set, which is the 2nd smallest element in the original list. 