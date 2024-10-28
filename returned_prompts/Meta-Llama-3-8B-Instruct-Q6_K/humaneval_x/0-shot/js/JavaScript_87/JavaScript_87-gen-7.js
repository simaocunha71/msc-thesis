Here is a Python solution for the problem:

```python
def getRow(lst, x):
    result = []
    for i, row in enumerate(lst):
        if x in row:
            result.append((i, row.index(x)))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

This function iterates over each row in the list, checks if the element `x` is present in the row, and if it is, appends the row index and the index of `x` in the row to the result list. After that, it sorts the result list based on the row index and the column index in descending order. Finally, it returns the sorted result list.