Here is a Python solution:

```Python
def getRow(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, element in enumerate(row):
            if element == x:
                result.append((i, j))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```

This function iterates over each row in the list, and for each row, it iterates over each element. If the element is equal to x, it adds the coordinate (i, j) to the result list. After all coordinates are found, it sorts the result list based on the row index and the column index in descending order. Finally, it returns the result list.

For example, when you call `getRow([[1,2,3,4,5,6], [1,2,3,4,1,6], [1,2,3,4,5,1]], 1)`, it will return `[(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]`. When you call `getRow([], 1)`, it will return `[]`. When you call `getRow([[], [1], [1, 2, 3]], 3)`, it will return `[(2, 2)]`. 