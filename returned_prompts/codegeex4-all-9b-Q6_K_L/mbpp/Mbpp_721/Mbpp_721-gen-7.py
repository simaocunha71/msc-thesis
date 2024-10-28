def maxAverageOfPath(matrix):
    total = 0
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        total += matrix[i][0]
    for j in range(1, cols):
        total += matrix[rows - 1][j]
    max_sum = total
    max_row = rows - 1
    max_col = cols - 1
    for i in range(rows - 2, -1, -1):
        max_sum = max_sum - matrix[i + 1][0] + matrix[i][max_col]
        max_row = i
        if max_sum > max_sum:
            max_sum = max_sum
            max_row = i
    for j in range(max_col - 1, -1, -1):
        max_sum = max_sum - matrix[max_row][j + 1] + matrix[max_row][j]
        max_col = j
        if max_sum > max_sum:
            max_sum = max_sum
            max_col = j
    return max_sum / (max_row + max_col + 1)

