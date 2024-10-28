def magic_square_test(matrix):
    # Flatten the matrix and sort the result
    flat_list = [row[col] for row in matrix for col in range(len(matrix))]
    flat_list.sort()

    # If the sorted result is not equal to the original, then it's not a magic square
    return flat_list == list(map(sum, zip(*matrix)))