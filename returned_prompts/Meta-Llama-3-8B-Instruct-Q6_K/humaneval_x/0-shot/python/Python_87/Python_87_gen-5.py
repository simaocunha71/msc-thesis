```
def get_row(lst, x):
    result = [(i, j) for i, sublst in enumerate(lst) for j, val in enumerate(sublst) if val == x]
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```



The function get_row(lst, x) takes a 2D list lst and an integer x as input. It iterates over each sub-list (row) in lst and each element in the sub-list. If the element is equal to x, it adds a tuple (row index, column index) to the result list. The result list is then sorted first by row index and then by column index in descending order.

The lambda function in the sort method is used to specify the sorting key. In this case, it sorts first by the row index (x[0]) and then by the column index (x[1]) in descending order (-x[1]). This is because the sort method in Python sorts in ascending order by default. The negative sign in front of x[1] reverses the order, making it descending.

The function finally returns the sorted result list. If the input list is empty or x is not found in the list, the function returns an empty list.