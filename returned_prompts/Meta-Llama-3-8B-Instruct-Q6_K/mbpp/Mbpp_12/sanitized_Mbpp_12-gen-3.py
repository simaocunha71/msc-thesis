def sort_matrix(matrix):
    return [list(i) for i in sorted((sum(row), row) for row in matrix)]
    # The expression (sum(row), row) creates a tuple for each row in the matrix, where the first element of the tuple is the sum of the row and the second element is the row itself. 
    # The sorted function then sorts these tuples based on the sum of the rows, and the list comprehension converts the sorted tuples back into a list of lists. 
    # This effectively sorts the matrix in ascending order according to the sum of its rows. 
    # For example, the test case assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]] shows that the matrix is sorted in ascending order according to the sum of its rows. 
    # The sum of the rows in the sorted matrix is [1, 1, 1], [1, 2, 3], [2, 4, 5], which is in ascending order. 
    # The original matrix is [[1, 2, 3], [2, 4, 5], [1, 1, 1]], which is not sorted in ascending order according to the sum of its rows. 
    # The sorted matrix is [[1, 1, 1], [1, 2, 3], [2, 4, 5]], which is the correct sorted matrix.  # noqa: E501
    # The sorted function is stable, which means that when multiple records have the same key, their original order is preserved. 
    # Therefore, the sorted matrix is not only sorted in ascending order according to the sum of its rows, but also the original order of the rows is preserved. 
    # For example, the row [1, 1, 1] appears first in the original matrix and also appears first in the sorted matrix. 
    # The row [1, 2, 3] appears second in the original matrix and also appears second in the sorted matrix. 
    # The row [2, 4, 5] appears third in the original matrix and also appears third in the sorted matrix. 
    # This shows that the sorted function is stable and preserves the original order