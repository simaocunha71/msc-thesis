```
def get_row(lst, x):
    result = [(i, j) for i, row in enumerate(lst) for j, val in enumerate(row) if val == x]
    result.sort(key=lambda x: (x[0], -x[1]))
    return result
```


Explanation:
The function `get_row` takes a 2D list `lst` and an integer `x` as input. It returns a list of tuples, where each tuple is a coordinate (row, column) in the 2D list, such that the value at that coordinate is `x`.

First, it generates a list of coordinates using a list comprehension. For each row `i` in the 2D list, it iterates over each value `j` in the row. If the value is equal to `x`, it adds the coordinate `(i, j)` to the result list.

Then, it sorts the result list in ascending order by row and descending order by column using the `sort` method and a lambda function as the sorting key. The lambda function returns a tuple `(x[0], -x[1])`, where `x[0]` is the row and `-x[1]` is the column (with the negative sign to sort in descending order).

Finally, it returns the sorted result list. If there are no coordinates with value `x` in the 2D list, the function returns an empty list. If there is only one coordinate with value `x`, the function still returns a list with a single tuple. If there are multiple coordinates with value `x`, the function returns a list of tuples with those coordinates. For example, if the input is `get_row([[1,2,3,4,5,6], [1,2,3,4,1,6], [1,2,3,4,5,1]], 1)`, the output is `[(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]`. If the input is `get_row([], 1)`, the output is an empty list. If the input is `get_row([[], [1], [1, 2, 3]], 3)`, the output is `[(2, 2)]`.