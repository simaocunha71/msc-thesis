```
def count_list(lst):
    count = 0
    for inner_list in lst:
        if isinstance(inner_list, list):
            count += 1
    return count
```
