```
def max_of_nth(matrix, n):
    return max(row[n] for row in matrix)
```
This function uses a generator expression to iterate over each row in the matrix, and for each row, it gets the `n`-th element (i.e., the element at column `n`). It then uses the built-in `max` function to find the maximum of these elements.

For example, if we call `max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2)`, it will return `19`, which is the maximum value in the third column.