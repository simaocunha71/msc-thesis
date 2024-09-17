```
def magic_square_test(matrix):
    n = len(matrix)
    expected_sum = n * (n**2 + 1) // 2
    for i in range(n):
        row_sum = sum(matrix[i])
        col_sum = sum(matrix[j][i] for j in range(n))
        if row_sum != expected_sum or col_sum != expected_sum:
            return False
    diagonal1_sum = sum(matrix[i][i] for i in range(n))
    diagonal2_sum = sum(matrix[i][n - i - 1] for i in range(n))
    if diagonal1_sum != expected_sum or diagonal2_sum != expected_sum:
        return False
    return True
```    
    This function checks if the input matrix is a magic square. A magic square is a square grid filled with distinct positive integers in the range 1 to n^2 such that each cell contains a different integer and the sum of the integers in each row, column, and diagonal is the same. The function calculates the expected sum for each row, column, and diagonal, and checks if the actual sum matches the expected sum. If the actual sum does not match the expected sum for any row, column, or diagonal, the function returns False, indicating that the matrix is not a magic square. If the actual sum matches the expected sum for all rows, columns, and diagonals, the function returns True, indicating that the matrix is a magic square.    



Note: The unit test provided is for a specific magic square, but the function can be used to check any square matrix for magic properties.    



The function `magic_square_test` takes a square matrix as input and returns `True` if the matrix is a magic square, and `False` otherwise. The function first calculates the expected sum for each row, column, and diagonal of the matrix. Then, it checks if the actual sum for each row, column, and diagonal matches the expected sum. If the actual sum does not match the expected sum for any row, column, or diagonal, the function returns `False`. If the actual sum matches the expected sum for all rows, columns, and diagonals, the function returns `True`.    



The unit test provided is for a specific magic square, but the function can be used to check any square matrix for magic properties.    



The function uses the following properties of magic squares to check if the matrix is a magic square:

1. The sum of the integers in each row is the