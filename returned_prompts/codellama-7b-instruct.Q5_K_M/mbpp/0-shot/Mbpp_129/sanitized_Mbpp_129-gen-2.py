def magic_square_test(matrix):
    # 1. Check if the matrix is a square.
    if len(matrix) != len(matrix[0]):
        return False

    # 2. Check if the sum of each row is equal to the same number.
    row_sums = [sum(row) for row in matrix]
    if len(set(row_sums)) != 1:
        return False

    # 3. Check if the sum of each column is equal to the same number.
    column_sums = [sum(col) for col in zip(*matrix)]
    if len(set(column_sums)) != 1:
        return False

    # 4. Check if the sum of all the elements is equal to the square of the number of rows.
    sum_of_elements = sum(sum(row) for row in matrix)
    if sum_of_elements != len(matrix) ** 2:
        return False

    return True