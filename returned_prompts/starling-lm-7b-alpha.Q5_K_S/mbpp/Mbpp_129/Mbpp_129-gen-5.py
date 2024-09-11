Here's one way you could write the function:

```python
def magic_square_test(matrix):
    n = len(matrix)
    if n == 0 or n != len(matrix[0]) or not all(len(row) == n for row in matrix):
        return False
    row_sum = sum(matrix[i][i] for i in range(n))
    col_sum = sum(matrix[i][i%n] for i in range(n))
    diag1 = sum(matrix[i][i] for i in range(n))
    diag2 = sum(matrix[i][n-1-i] for i in range(n))
    return (row_sum == col_sum == diag1 == diag2) and all(sum(row) == row_sum for row in matrix) and \
        all(sum(col) == col_sum for col in zip(*matrix))
```

This function checks if the matrix is a magic square by first making sure the matrix has a square shape and all the rows and columns have the same length. It then calculates the sum of the elements in the main diagonal, the sum of the elements in the anti-diagonal, and the sum of the elements in each row and column. If all of these sums are equal, the matrix is a magic square.

For example, if you call `magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])`, it will return `True` because all the conditions are met.

```python
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True
```

```python
assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3,