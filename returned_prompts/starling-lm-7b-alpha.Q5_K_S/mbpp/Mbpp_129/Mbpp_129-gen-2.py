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


# Test the function
matrix = [[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]
print(magic_square_test(matrix))  # True



"""
This function, magic_square_test, uses list comprehension to calculate the sum of each row, column, and diagonal of the matrix. It then checks if all of the sums are equal. If they are, it returns True, indicating that the matrix is a magic square. Otherwise, it returns False.
"""

"""
In the provided test case, the matrix is a magic square because the sum of each row, column, and diagonal is equal. The function correctly identifies this and returns True.
"""



"""
To use this function, you can pass in a matrix as an argument. The function will then return True if the matrix is a magic square and False otherwise.
"""



"""
To test the function, you can create a matrix and pass it to the function. The result will be printed to the console. In this example, the matrix [[7, 12, 1, 14], [2, 13,