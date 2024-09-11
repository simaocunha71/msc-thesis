```
def sort_matrix(matrix):
    matrix = sorted(matrix, key=lambda x: sum(x))
    return matrix
```

Here is a Python function that sorts a matrix according to the sum of its rows. The `sorted` function is used with a `lambda` function as the `key` parameter. The `lambda` function calculates the sum of each row and sorts the matrix based on the sums.

The `sort_matrix` function takes a matrix as input and returns the sorted matrix. The `lambda` function `lambda x: sum(x)` is used to calculate the sum of each row `x` in the matrix. This sum is used as the key for sorting the rows of the matrix in ascending order.

The `sorted` function is a built-in Python function that sorts the elements of a list in ascending order by default. In this case, it is used to sort the rows of the matrix based on the sums of the rows. The sorted matrix is then returned by the `sort_matrix` function.

The `assert` statement is used to check if the `sort_matrix` function correctly sorts the given matrix. In the example provided, the function correctly sorts the matrix `[[1, 2, 3], [2, 4, 5], [1, 1, 1]]` and the result is `[[1, 1, 1], [1, 2, 3], [2, 4, 5]]`.

Overall, this solution provides a simple and efficient way to sort a matrix based on the sum of its rows in Python.

```python
def sort_matrix(matrix):
    matrix = sorted(matrix, key=lambda x: sum(x))
    return matrix
```

```python
# Test Case
print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))  # Output: [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
```

This test case demonstrates that the `sort_matrix` function correctly sorts the given matrix according to the sum of its rows.

```python
# Test Case 2