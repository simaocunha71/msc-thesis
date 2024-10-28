def magic_square_test(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)
    expected_sum = n * (n * n + 1) // 2
    for i in range(n):
        row_sum = sum(matrix[i])
        if row_sum != expected_sum:
            return False
        col_sum = sum(matrix[j][i] for j in range(n))
        if col_sum != expected_sum:
            return False
    diag_sum = sum(matrix[i][i] for i in range(n))
    if diag_sum != expected_sum:
        return False
    diag_sum = sum(matrix[i][n-i-1] for i in range(n))
    if diag_sum != expected_sum:
        return False
    return True
print(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))  #True

This function checks whether a given matrix is a magic square or not. A magic square is a square matrix filled with distinct positive integers in such a way that the sum of each row, each column, and each diagonal is equal and is called the magic constant. The function first checks if the matrix is a square (i.e., has the same number of rows and columns). If not, it returns False. Then it calculates the expected sum for a magic square of the given size. It checks if each row, each column, and both diagonals have the expected sum. If any of these sums is different from the expected sum, the function returns False. If all sums are equal to the expected sum, the function returns True, indicating that the matrix is a magic square. 

Note: This function assumes that the input is a valid matrix (i.e., a list of lists where each inner list has the same length). It does not check for this, as it is assumed to be the case by the problem statement. If the input might not be a valid matrix, you should add error checking code to handle this possibility. 









