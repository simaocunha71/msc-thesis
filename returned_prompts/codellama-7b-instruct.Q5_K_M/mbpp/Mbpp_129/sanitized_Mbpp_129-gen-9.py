def magic_square_test(matrix):
    # Check shape of matrix
    if len(matrix) != len(matrix[0]) or len(matrix) % 2 == 1:
        return False
    # Check that all elements are positive integers
    for row in matrix:
        for element in row:
            if element < 1 or not isinstance(element, int):
                return False
    # Check that sum of rows is 15
    for row in matrix:
        if sum(row) != 15:
            return False
    # Check that sum of columns is 15
    for i in range(len(matrix[0])):
        column_sum = 0
        for row in matrix:
            column_sum += row[i]
        if column_sum != 15:
            return False
    # Check that diagonals sum is 15
    diagonal1_sum = 0
    for i in range(len(matrix)):
        diagonal1_sum += matrix[i][i]
    diagonal2_sum = 0
    for i in range(len(matrix)):
        diagonal2_sum += matrix[i][len(matrix[0]) - i - 1]
    if diagonal1_sum != 15 or diagonal2_sum != 15:
        return False
    return True