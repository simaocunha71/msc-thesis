def magic_square_test(matrix):
    # Calculate the sum of each row
    row_sums = [sum(row) for row in matrix]

    # Calculate the sum of each column
    col_sums = [sum(col) for col in zip(*matrix)]

    # Calculate the sum of the two diagonals
    diag_sums = [sum(row[i] for row in matrix) for i in range(len(matrix))]
    diag_sums.append(sum(row[-i - 1] for i, row in enumerate(matrix))[::-1])

    # Check if all sums are equal
    return all(sum_1 == sum_2 for sum_1, sum_2 in zip(row_sums, col_sums)) and all(sum_1 == sum_2 for sum_1, sum_2 in zip(diag_sums, col_sums))
matrix = [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]