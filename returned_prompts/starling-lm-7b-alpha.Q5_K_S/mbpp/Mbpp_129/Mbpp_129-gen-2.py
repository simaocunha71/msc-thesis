
def magic_square_test(matrix):
    return all(sum(row) == sum(matrix[-1]) for row in matrix) and all(sum(col) == sum(matrix[0]) for col in zip(*matrix)) and all(sum(matrix[i][i] for i in range(len(matrix))) == sum(matrix[i][(i+1)%len(matrix)]) for i in range(len(matrix)))


