```
def second_smallest(lst):
    if len(lst) < 2:
        raise ValueError("List must have at least two elements")

    sorted_lst = sorted(set(lst))
    if len(sorted_lst) < 2:
        raise ValueError("List must have at least two unique elements")

    return sorted_lst[1]
```







