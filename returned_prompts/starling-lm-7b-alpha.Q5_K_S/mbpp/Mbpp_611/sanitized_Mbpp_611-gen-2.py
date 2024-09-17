def max_of_nth(matrix, n):
    max_num = 0
    for i in range(len(matrix)):
        if matrix[i][n-1] > max_num:
            max_num = matrix[i][n-1]
    return max_num