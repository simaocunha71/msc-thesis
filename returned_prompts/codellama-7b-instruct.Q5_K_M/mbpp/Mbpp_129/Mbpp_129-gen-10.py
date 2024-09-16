def magic_square_test(matrix):
    rows_sum = [sum(row) for row in matrix]
    cols_sum = [sum(col) for col in zip(*matrix)]
    diag_sum = sum(matrix[i][i] for i in range(len(matrix)))
    anti_diag_sum = sum(matrix[i][len(matrix)-i-1] for i in range(len(matrix)))
    sums = [sum(matrix[i]) for i in range(len(matrix))]
    return (sum(sums) in sums) and (max(sums)-min(sums)==2)

# 1.1.6
