"""
def flatten_list(lst):
    res = []
    for i in lst:
        if isinstance(i, list):
            res.extend(flatten_list(i))
        else:
            res.append(i)
    return res


flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])

"""

def flatten_list(lst):
    res = []
    for i in lst:
        if isinstance(i, list):
            res.extend(flatten_list(i))
        else:
            res.append(i)
    return res


flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])


```

```

```