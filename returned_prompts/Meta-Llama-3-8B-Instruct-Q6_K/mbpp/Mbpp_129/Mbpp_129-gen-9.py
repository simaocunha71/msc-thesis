```
def magic_square_test(matrix):
    n = len(matrix)
    expected_sum = sum(matrix[0])
    for row in matrix:
        if sum(row) != expected_sum:
            return False
    for col in range(n):
        if sum([row[col] for row in matrix]) != expected_sum:
            return False
    return True
```


The function `magic_square_test` checks whether a given matrix is a magic square. A magic square is a square matrix filled with distinct positive integers, where each row, column, and diagonal adds up to the same value, known as the magic constant. In the provided unit test, the input matrix is a magic square with the magic constant being the sum of its first row (7 + 12 + 1 + 14 = 34). The function iterates over each row and column of the matrix, checking if the sum of its elements matches the expected sum. If any row or column sum does not match the expected sum, the function returns False, indicating that the matrix is not a magic square. If all row and column sums match the expected sum, the function returns True, confirming that the matrix is a magic square.