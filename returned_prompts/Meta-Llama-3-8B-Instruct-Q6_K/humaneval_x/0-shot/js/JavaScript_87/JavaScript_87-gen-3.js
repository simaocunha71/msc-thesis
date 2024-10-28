Here is a Python solution for the problem. This function loops over each row in the list, and for each row, it checks if the value is equal to the given x. If it is, it adds the coordinates (row index, column index) to the result list. The result list is then sorted based on the row index in ascending order and column index in descending order.

```Python
def getRow(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, value in enumerate(row):
            if value == x:
                result.append((i, j))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```


This function works by first looping over each row in the list. For each row, it then loops over each value in the row. If the value is equal to the given x, it adds the coordinates (row index, column index) to the result list. The result list is then sorted based on the row index in ascending order and column index in descending order. This is done using the built-in sort function with a lambda function as the key. The lambda function returns a tuple for each coordinate in the result list. The tuple contains the row index and the negative of the column index. The negative of the column index is used to sort the column indices in descending order. The sorted result list is then returned.