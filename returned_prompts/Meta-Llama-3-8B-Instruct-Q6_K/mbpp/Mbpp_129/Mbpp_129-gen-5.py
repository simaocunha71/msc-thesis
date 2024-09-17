```
def magic_square_test(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)
    expected_sum = n * (n**2 + 1) // 2
    for i in range(n):
        if sum(matrix[i]) != expected_sum:
            return False
        row_sum = sum(matrix[i])
        if row_sum != expected_sum:
            return False
    return True
```
The function checks if the input matrix is a magic square. A magic square is a square matrix filled with distinct positive integers in such a way that the sum of each row, each column, and each diagonal is equal. The function takes a matrix as input and returns True if it is a magic square and False otherwise.

The function first checks if the matrix is a square (i.e., if the number of rows is equal to the number of columns). If it is not a square, the function returns False.

Then, it calculates the expected sum for each row, which is the sum of the first n natural numbers, where n is the size of the matrix. This is calculated as n * (n^2 + 1) / 2.

The function then checks if the sum of each row is equal to the expected sum. If any row sum is not equal to the expected sum, the function returns False.

Finally, the function checks if the sum of each column is equal to the expected sum. If any column sum is not equal to the expected sum, the function returns False.

If the function has not returned False by this point, it means that the matrix is a magic square, so the function returns True.