```
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        for j, element in enumerate(row):
            if element == x:
                result.append((i, j))
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```


In this function, we iterate over each row and each element in the row. If the element is equal to `x`, we append the coordinates (i, j) to our result list. After we have checked all elements, we sort the result list based on the row index and the column index. We sort the row index in ascending order and the column index in descending order. This is done using a lambda function as the key for the sort method. Finally, we return the sorted result list. 

The time complexity of this function is O(n*m) where n is the number of rows and m is the maximum number of columns. This is because we are iterating over each element in the list once. The space complexity is O(n*m) as well, because in the worst case, we might need to store all elements in the result list. 

This function passes all the given examples. For example, `get_row([[1,2,3,4,5,6], [1,2,3,4,1,6], [1,2,3,4,5,1]], 1)` returns `[(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]`. `get_row([], 1)` returns an empty list, and `get_row([[], [1], [1, 2, 3]], 3)` returns `[(2, 2)]`. 