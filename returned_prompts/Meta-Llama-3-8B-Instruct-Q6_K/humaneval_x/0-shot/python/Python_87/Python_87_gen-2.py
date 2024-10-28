
The problem is asking you to find all occurrences of a given number `x` in a 2D list (a list of lists), and return the coordinates of those occurrences as a list of tuples. The coordinates are in the format `(row, column)`, where `row` is the index of the sublist in the 2D list, and `column` is the index of the element in the sublist. The coordinates should be sorted first by row in ascending order, and then by column in descending order.

Here is the solution:
```
def get_row(lst, x):
    result = []
    for i, row in enumerate(lst):
        if x in row:
            for j, val in enumerate(reversed(row)):
                if val == x:
                    result.append((i, len(row) - j - 1))
    return sorted(result, key=lambda x: (x[0], -x[1]))
```
This function iterates over each sublist in the 2D list, and checks if the given number `x` is in the sublist. If it is, it finds the last occurrence of `x` in the sublist (because we're iterating in reverse order) and appends the coordinates `(i, len(row) - j - 1)` to the result list. Finally, it sorts the result list using the `sorted` function with a custom sorting key that first sorts by row in ascending order, and then by column in descending order. The `-x[1]` part in the sorting key is used to sort the columns in descending order.

For example, if the input is `[[1,2,3,4,5,6], [1,2,3,4,1,6], [1,2,3,4,5,1]]` and `x` is `1`, the output will be `[(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]`, which are the coordinates of the occurrences of `1` in the 2D list. The coordinates are sorted first