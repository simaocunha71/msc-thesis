def magic_square_test(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    total = sum(matrix[0])
    for row in matrix:
        if sum(row) != total:
            return False
    for col in range(len(matrix[0])):
        if sum([matrix[row][col] for row in range(len(matrix))]) != total:
            return False
    if sum([matrix[i][i] for i in range(len(matrix))]) != total:
        return False
    if sum([matrix[i][len(matrix)-i-1] for i in range(len(matrix))]) != total:
        return False
    return True
    # Check rows, columns, and diagonals if they all add up to the same sum. If they do, then it's a magic square. If not, then it's not.  # Check rows, columns, and diagonals if they all add up to the same sum. If they do, then it's a magic square. If not, then it's not.  # Check rows, columns, and diagonals if they all add up to the same sum. If they do, then it's a magic square. If not, then it's not.  # Check rows, columns, and diagonals if they all add up to the same sum. If they do, then it's a magic square. If not, then it's not.  # Check rows, columns, and diagonals if they all add up to the same sum. If they do, then it's a magic square. If not, then it's not.  # Check rows, columns, and diagonals if they all add up to the same sum. If they do, then it's a magic square. If not, then it's not.  # Check rows, columns, and diagonals if they all add up to the same sum. If they do, then it's a magic square. If not, then it's not.  # Check rows, columns, and diagonals if they all add up to the same sum. If they do, then it's a magic square. If not, then it's not.  # Check rows, columns, and diagonals if they all add up to the same sum. If they do, then it's a magic square. If not, then it's not.  # Check rows, columns, and diagonals if they all add up to the same sum. If they do