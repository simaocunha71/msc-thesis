A magic square is a grid of numbers where the sums of the numbers in each row, each column, and both diagonals are the same. This function will check if a given matrix is a magic square by comparing the sums of the elements in each row, column, and the two diagonals.

Here is a Python function that accomplishes this:

```python
def magic_square_test(matrix):
    # Get the size of the matrix
    size = len(matrix)

    # Initialize the sums for the rows, columns and diagonals
    row_sums = [0]*size
    col_sums = [0]*size
    diag_sum1 = 0
    diag_sum2 = 0

    # Calculate the sums
    for i in range(size):
        for j in range(size):
            row_sums[i] += matrix[i][j]
            col_sums[j] += matrix[i][j]
            if i == j:
                diag_sum1 += matrix[i][j]
            if i + j == size - 1:
                diag_sum2 += matrix[i][j]

    # Check if all sums are the same
    if len(set(row_sums)) == 1 and len(set(col_sums)) == 1 and diag_sum1 == diag_sum2 == row_sums[0] == col_sums[0]:
        return True
    else:
        return False
```

In the above function, we first calculate the sums of the elements in each row, each column, and the two diagonals. Then, we check if all these sums are the same. If they are, the matrix is a magic square. Otherwise, it is not.

We use sets to check if all sums are the same because a set in Python only contains unique elements. If all elements in a set are the same, the length of the set is 1.

This function assumes that the input matrix is a square matrix (i.e., the number of rows is the same as the number of columns). If this is not the case, you would need to add error checking to handle non-square matrices.

This function also assumes that the matrix contains positive integers. If the matrix can contain