A magic square is a square grid filled with distinct positive integers such that each cell contains a different integer and the sum of the integers in each row, each column, and both diagonals is the same.

Here is a Python function to check if a given matrix is a magic square or not:

```python
def magic_square_test(matrix):
    # Get the size of the matrix
    size = len(matrix)
    
    # Calculate the magic constant
    magic_constant = size * (size * size + 1) // 2

    # Check rows and columns
    for i in range(size):
        if sum(matrix[i]) != magic_constant or sum(matrix[j][i] for j in range(size)) != magic_constant:
            return False

    # Check diagonals
    if sum(matrix[i][i] for i in range(size)) != magic_constant or sum(matrix[i][size - i - 1] for i in range(size)) != magic_constant:
        return False

    return True

assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]) == True
```

The function works by first calculating the magic constant (the sum of the numbers in one row or column), then checking each row and column. If any row or column sums to a different number, the function returns False, indicating that the matrix is not a magic square. It also checks the sums of the two diagonals. If either diagonal sum differs from the magic constant, it returns False, indicating that the matrix is not a magic square. If all the checks pass, the function returns True, indicating that the matrix is a magic square.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:
<jupyter_code>
"""
