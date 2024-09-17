```
def sort_matrix(matrix):
    return [row for _, row in sorted((sum(row), row) for row in matrix)]
```





The task is to create a function that sorts a given 2D matrix in ascending order based on the sum of its rows. The function should return the sorted matrix.

The provided unit test helps in understanding the problem better. It shows that the matrix [[1, 2, 3], [2, 4, 5], [1, 1, 1]] should be sorted as [[1, 1, 1], [1, 2, 3], [2, 4, 5]].

To solve this problem, we can use a list comprehension and the built-in sorted function in Python. We first calculate the sum of each row using a generator expression, then sort the rows based on these sums, and finally use a list comprehension to create the sorted matrix.

Here's the Python function that accomplishes this:

```python
def sort_matrix(matrix):
    return [row for _, row in sorted((sum(row), row) for row in matrix)]
```

This function works by first creating a list of tuples, where each tuple contains the sum of a row and the row itself. The sorted function is then used to sort this list of tuples based on the sums. Finally, the list comprehension is used to create a new list containing the sorted rows. The `_` variable is used to ignore the sum values, since we're only interested in the sorted rows.