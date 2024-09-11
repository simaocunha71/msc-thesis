```
def sort_matrix(matrix):
    def row_sum(row):
        return sum(row)
    return sorted(matrix, key=row_sum)
```

Explanation:
The function `sort_matrix` takes a matrix as input and uses the `sorted` function to sort the matrix. The `key` parameter of the `sorted` function is set to `row_sum`, which is a function that computes the sum of a row. By using `row_sum` as the key, the `sorted` function will sort the rows of the matrix based on the sum of the rows in ascending order.

In the provided example, the `sort_matrix` function is called with the matrix `[[1, 2, 3], [2, 4, 5], [1, 1, 1]]`. The `row_sum` function is used as the key to sort the matrix. The resulting sorted matrix is `[[1, 1, 1], [1, 2, 3], [2, 4, 5]]`.

This solution demonstrates how to sort a matrix based on the sum of its rows in ascending order using the `sorted` function and a custom key.

Note: The provided solution assumes that the input matrix is a list of lists, where each inner list represents a row of the matrix.

Here are some additional test cases that can be used to validate the correctness of the `sort_matrix` function:

```python
print(sort_matrix([[3, 2, 1], [1, 1, 3], [2, 2, 2]]))  # Output: [[1, 1, 2], [1, 2, 2], [2, 2, 3]]
print(sort_matrix([[5, 4, 3], [2, 2, 1], [3, 3, 3]]))  # Output: [[2, 2, 1], [3, 3, 3], [5, 4, 3]]
print(sort_matrix([[10, 9, 8], [7, 6, 5], [4, 3, 2], [1, 0, 1]]