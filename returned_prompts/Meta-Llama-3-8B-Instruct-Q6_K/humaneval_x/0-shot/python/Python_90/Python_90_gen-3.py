```
def next_smallest(lst):
    if len(lst) < 2:
        return None
    lst.sort()
    for i in range(len(lst) - 1):
        if lst[i] != lst[i+1]:
            return lst[i+1]
    return None
```


Explanation:
The function first checks if the list has less than 2 elements. If it does, it returns None. Then, it sorts the list. It then iterates over the list, checking each element with the next one. If it finds a pair of different elements, it returns the second element of the pair. If it doesn't find any pair of different elements, it means the list has only one element or all elements are the same, so it returns None.