
def average_of_nth(matrix, n):
    return sum(row[n] for row in matrix) / len(matrix)

print(average_of_nth([[