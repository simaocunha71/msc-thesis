"""
To sort a matrix in ascending order according to the sum of its rows, you can follow these steps:

1. Calculate the sum of each row in the matrix. This can be done using the built-in sum() function in Python, applied to each row of the matrix.
2. Sort the rows based on the sum of their elements. Python provides a built-in function called sorted() that can be used to sort a list of values. In this case, you can pass a lambda function to the sorted() function to calculate the sum of each row and use it as the key for sorting.
3. Create a new matrix with the sorted rows. Iterate through the sorted rows and add them to a new matrix in the same order.
4. Return the new matrix as the result.
Here's a Python function that implements these steps:

def sort_matrix(matrix):
    # Step 1: Calculate the sum of each row
    row_sums = [sum(row) for row in matrix]
    
    # Step 2: Sort the rows based on the sum of their elements
    sorted_rows = sorted(matrix, key=lambda row: sum(row))
    
    # Step 3: Create a new matrix with the sorted rows
    sorted_matrix = []
    for row in sorted_rows:
        sorted_matrix.append(row)
    
    # Step 4: Return the new matrix
    return sorted_matrix
"""

def sort_matrix(matrix):
    # Step 1: Calculate the sum of each row
    row_sums = [sum(row) for row in matrix]
    
    # Step 2: Sort the rows based on the sum of their elements
    sorted_rows = sorted(matrix, key=lambda row: sum(row))
    
    # Step 3: Create a new matrix with the sorted rows
    sorted_matrix = []
    for row in sorted_rows:
        sorted_matrix.append(row)
    
    # Step 4: Return the new matrix
    return sorted_matrix

# Test the function
matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print(sort_matrix(matrix) == [[1