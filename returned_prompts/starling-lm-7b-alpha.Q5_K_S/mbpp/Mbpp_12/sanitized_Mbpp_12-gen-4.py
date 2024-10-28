def sort_matrix(matrix):
    # Flatten the matrix into a 1D array
    flat_array = [num for sublist in matrix for num in sublist]
    
    # Sort the array in ascending order based on the sum of rows
    sorted_array = sorted(flat_array, key=lambda x: sum(x))
    
    # Reshape the sorted array back into a matrix
    sorted_matrix = [sorted_array[i:i+len(matrix[0])] for i in range(0, len(sorted_array), len(matrix[0]))]
    
    return sorted_matrix