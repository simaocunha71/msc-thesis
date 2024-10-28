```
def next_smallest(lst):
    if len(lst) < 2:
        return None
    lst.sort()
    if lst[0] == lst[1]:
        return None
    return lst[1]
```


The next_smallest() function first checks if the list has less than 2 elements. If so, it returns None. Then it sorts the list. If the first two elements are equal, it means there is no second smallest element in the list, so it returns None. Otherwise, it returns the second smallest element, which is the first element after sorting the list.