"""
Here is a Python program to solve the problem:


def sort_matrix(matrix):
    # Sort the matrix by the sum of its rows
    sorted_matrix = sorted(matrix, key=lambda x: sum(x))
    return sorted_matrix

# Test the function
matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print(sort_matrix(matrix))  # Output: [[1, 1, 1], [1, 2, 3], [2, 4, 5]]

"""
Here is the explanation of the above code:

The function `sort_matrix` takes a matrix as input and returns the sorted matrix. It uses the `sorted` function with a `key` parameter to sort the matrix based on the sum of its rows. The `key` parameter is a function that takes a row (a list) as input and returns the sum of the row. The `sorted` function sorts the matrix based on these sums in ascending order. Finally, the function returns the sorted matrix.

The test case checks if the `sort_matrix` function correctly sorts the given matrix and prints the result.

The output of the test case is `[[1, 1, 1], [1, 2, 3], [2, 4, 5]]`, which is the sorted matrix according to the sum of its rows.

"""

def sort_matrix(matrix):
    # Sort the matrix by the sum of its rows
    sorted_matrix = sorted(matrix, key=lambda x: sum(x))
    return sorted_matrix

# Test the function
matrix = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print(sort_matrix(matrix))  # Output: [[1, 1, 1], [1, 2, 3], [2, 4, 5]]

```
In the above code, the `sort_matrix` function takes a matrix as input and returns the sorted matrix. The `sorted` function is used with a `key` parameter to sort the matrix based on the sum of its rows. The `key` parameter is a function that takes