```
def sort_matrix(matrix):
    matrix_sums = []
    for i in matrix:
        matrix_sums.append(sum(i))
    sorted_sums = sorted(matrix_sums)
    sorted_matrix = []
    for i in sorted_sums:
        sorted_matrix.append(list(filter(lambda x: sum(x) == i, matrix)))
    return sorted_matrix
```

This function first calculates the sum of each row in the matrix and stores it in a new list called `matrix_sums`. Then, it sorts `matrix_sums` in ascending order. Next, it initializes an empty list called `sorted_matrix`. It iterates over the sorted sums and, for each sum, it finds the corresponding row(s) in the original matrix by using a filter function. The found row(s) are appended to `sorted_matrix`. Finally, `sorted_matrix` is returned as the result.

To verify the correctness of the function, you can run the provided assert statement with a sample matrix. It should return `[[1, 1, 1], [1, 2, 3], [2, 4, 5]]`.

This solution uses the built-in `sorted` function to sort the sums of the rows in ascending order. It also uses the `filter` function to find the rows with the corresponding sum in the original matrix.

Overall, this function provides a simple and effective way to sort a given matrix based on the sum of its rows in ascending order.

```python
def sort_matrix(matrix):
    matrix_sums = []
    for i in matrix:
        matrix_sums.append(sum(i))
    sorted_sums = sorted(matrix_sums)
    sorted_matrix = []
    for i in sorted_sums:
        sorted_matrix.append(list(filter(lambda x: sum(x) == i, matrix)))
    return sorted_matrix
```

This solution first calculates the sum of each row in the matrix and stores it in a new list called `matrix_sums`. Then, it sorts `matrix_sums` in ascending order. Next, it initializes an empty