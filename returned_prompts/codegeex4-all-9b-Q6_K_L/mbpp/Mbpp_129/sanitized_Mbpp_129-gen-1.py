def magic_square_test(matrix):
    # Check if the matrix is square
    if len(matrix) != len(matrix[0]):
        return False
    
    # Check if the sums of the rows are equal
    row_sums = [sum(row) for row in matrix]
    if len(set(row_sums)) != 1:
        return False
    
    # Check if the sums of the columns are equal
    col_sums = [sum(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]
    if len(set(col_sums)) != 1:
        return False
    
    # Check if the sums of the diagonals are equal
    diag1_sum = sum(matrix[i][i] for i in range(len(matrix)))
    diag2_sum = sum(matrix[i][len(matrix)-i-1] for i in range(len(matrix)))
    if diag1_sum != diag2_sum or len(set([diag1_sum, diag2_sum])) != 1:
        return False
    
    return True