Here's a Python function that can be used to test whether a given matrix is a magic square:

```python
def magic_square_test(matrix):
    # Check if all rows have the same sum
    row_sums = [sum(row) for row in matrix]
    if len(set(row_sums)) != 1:
        return False

    # Check if all columns have the same sum
    column_sums = [sum(col) for col in zip(*matrix)]
    if len(set(column_sums)) != 1:
        return False

    # Check if the diagonal sum is equal to the row/column sum
    diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
    if diagonal_sum != row_sums[0]:
        return False

    # Check if the anti-diagonal sum is equal to the row/column sum
    anti_diagonal_sum = sum(matrix[i][-1-i] for i in range(len(matrix)))
    if anti_diagonal_sum != row_sums[0]:
        return False

    return True
```

This function checks whether a given matrix is a magic square by verifying the following conditions:

- All rows in the matrix have the same sum.
- All columns in the matrix have the same sum.
- The sum of the elements in the main diagonal is equal to the sum of the elements in the first row.
- The sum of the elements in the anti-diagonal is equal to the sum of the elements in the first row.

If all these conditions are met, the function returns True, indicating that the matrix is a magic square. Otherwise, it returns False.

You can use this function to check whether the provided matrix is a magic square or not.

Here's an example of how to use the function:

```python
matrix = [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]
print(magic_square_test(matrix))  # Output: True
```