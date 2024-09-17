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
matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]