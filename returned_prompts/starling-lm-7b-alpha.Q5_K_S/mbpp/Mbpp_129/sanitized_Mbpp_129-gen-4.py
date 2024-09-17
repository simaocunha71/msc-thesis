def magic_square_test(matrix):
    # Flatten the matrix and convert to a list
    flat_matrix = [item for sublist in matrix for item in sublist]
    # Check if the flattened matrix is a permutation of 1 to N
    if sorted(flat_matrix) == list(range(1, len(flat_matrix)+1)):
        return True
    else:
        return False