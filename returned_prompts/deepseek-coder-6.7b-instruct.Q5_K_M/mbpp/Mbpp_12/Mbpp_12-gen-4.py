def sort_matrix(matrix):
    sums = [sum(row) for row in matrix]
    return [row for _, row in sorted(zip(sums, matrix))]

print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))

# OUTPUT:
# [[1, 1, 1], [1, 2, 3], [2, 4, 5]]

# Explanation:
# The sums of the rows in the given matrix are [6, 11, 4]. 
# So, the rows are sorted in ascending order based on these sums, 
# and the sorted matrix is [[1, 1, 1], [1, 2, 3], [2, 4, 5]].

# 