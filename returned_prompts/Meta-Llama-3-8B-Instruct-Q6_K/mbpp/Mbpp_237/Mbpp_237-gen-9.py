```
def check_occurences(lst):
    from collections import defaultdict
    dict = defaultdict(int)
    for item in lst:
        dict[tuple(sorted(item))] += 1
    return dict
```






