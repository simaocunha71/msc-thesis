
```python
def find_combinations(lst):
    res = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            res.append((lst[i][0] + lst[j][0], lst[i][1] + lst[j][1]))
            res.append((lst[i][0] + lst[j][1], lst[i][1] + lst[j][0]))
            res.append((lst[i][1] + lst[j][0], lst[i][0] + lst[j][1]))
            res.append((lst[i][1] + lst[j][1], lst[i][0] + lst[j][0]))
    return res

print(find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]))
```

This function works by iterating through the list of tuples and for each pair of tuples, it adds all possible combinations of sums to the result list. It uses list comprehension to generate all possible combinations and adds them to the result list.
"""

"""
