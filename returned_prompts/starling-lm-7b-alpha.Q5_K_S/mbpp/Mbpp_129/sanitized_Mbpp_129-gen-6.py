def magic_square_test(matrix):
    for row in matrix:
        if not all(map(lambda x: x in row, matrix[0])):
            return False
    for col in zip(*matrix):
        if not all(map(lambda x: x in col, col)):
            return False
    if sum(matrix[i][i] for i in range(len(matrix))) != sum(matrix[i][-1-i] for i in range(len(matrix))) != sum(matrix[i][len(matrix)-1-i] for i in range(len(matrix))) != sum(matrix[i][len(matrix)-1-i] for i in range(len(matrix))):
        return False
    return True
matrix = [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]