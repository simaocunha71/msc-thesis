def magic_square_test(matrix):
    # convert the matrix into a list
    flat_list = [item for sublist in matrix for item in sublist]

    # calculate the sum of the first row
    sum_row = sum(matrix[0])

    # create a list to store the sum of rows, cols and diags
    sum_list = []

    # calculate and store the sum of each row
    for row in matrix:
        sum_list.append(sum(row))

    # calculate and store the sum of each column
    for i in range(len(matrix[0])):
        sum_list.append(sum(row[i] for row in matrix))

    # calculate and store the sum of each diagonal
    sum_list.append(sum(matrix[i][i] for i in range(len(matrix))))
    sum_list.append(sum(matrix[i][len(matrix)-i-1] for i in range(len(matrix))))

    # check if all sums are equal to the sum of the first row
    for s in sum_list:
        if s != sum_row:
            return False

    return True


print(magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))  # True





