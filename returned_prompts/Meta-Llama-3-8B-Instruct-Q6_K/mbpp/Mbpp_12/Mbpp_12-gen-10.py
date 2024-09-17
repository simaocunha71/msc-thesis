```
def sort_matrix(matrix):
    return sorted(matrix, key=lambda x: sum(x))
```





The problem is asking to sort a given matrix in ascending order according to the sum of its rows. 

The unit test `assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]` helps to understand that the sorting should be based on the sum of the rows.

The solution uses the built-in `sorted` function in Python, and the `key` argument is set to a lambda function that calculates the sum of each row. The `sorted` function then sorts the matrix based on the sum of each row.

Here is the solution:
```
def sort_matrix(matrix):
    return sorted(matrix, key=lambda x: sum(x))
```





The function `sort_matrix` takes a matrix as input, calculates the sum of each row using the lambda function `lambda x: sum(x)`, and then sorts the matrix based on these sums. The result is a new matrix sorted in ascending order according to the sum of its rows.