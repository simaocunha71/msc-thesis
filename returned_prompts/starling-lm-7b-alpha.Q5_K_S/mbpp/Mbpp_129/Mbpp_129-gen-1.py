To determine whether a matrix is a magic square, we need to check if:
1. The matrix is a square matrix, i.e., the number of rows and columns are the same.
2. The matrix is symmetric, i.e., the elements in the upper triangle are the same as the corresponding elements in the lower triangle.
3. The sum of the elements in each row, each column, and each main diagonal is the same.
4. The sum of the elements in each of the other diagonals is the same.

Here's a Python function that checks these conditions:

```python
def is_magic_square(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    rows = set(sum(row) for row in matrix)
    cols = set(sum(col) for col in zip(*matrix))
    diags = set(sum(matrix[i][i] for i in range(len(matrix))) for _ in range(2))
    other_diags = set(sum(matrix[i][-1-i] for i in range(len(matrix))) for _ in range(2))
    return len(rows) == 1 and len(cols) == 1 and len(diags) == 1 and len(other_diags) == 1
```

This function first checks if the number of rows and columns are the same. If not, it returns False. Then, it calculates the sum of each row, column, and diagonal, and stores them in sets. If the length of any of these sets is not 1, it means that the corresponding sum is not unique, and the matrix is not a magic square. Finally, it returns True if all conditions are met, and False otherwise.

You can test this function with the provided example:

```python
matrix = [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]
print(is_magic_square(matrix))  # Output: True
```

This will return True, indicating that the matrix is a magic square.

```python
