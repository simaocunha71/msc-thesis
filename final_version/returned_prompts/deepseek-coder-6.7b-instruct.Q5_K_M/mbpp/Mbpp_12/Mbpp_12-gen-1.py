"""
def sort_matrix(matrix):
    # Calculate the sum of each row in the matrix and store the sums in a list
    sums = [sum(row) for row in matrix]
    # Sort the matrix based on the sums of its rows
    return [row for _, row in sorted(zip(sums, matrix))]
"""

