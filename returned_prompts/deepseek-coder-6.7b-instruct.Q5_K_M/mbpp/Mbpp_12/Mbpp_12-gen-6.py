"""
Firstly, the function will calculate the sum of each row in the matrix. Then, it will sort the matrix based on these sums.
"""

P:
"""
- Define a function `sort_matrix` that takes a matrix as input.
- Initialize an empty list `sums` to store the sums of the rows in the input matrix.
- Using a for loop, iterate through each row in the input matrix. For each row, calculate the sum using the built-in `sum` function, and append this sum to the `sums` list.
- Use the built-in `zip` function to create a list of tuples where each tuple contains a row from the input matrix and its corresponding sum from the `sums` list.
- Sort this list of tuples using the built-in `sorted` function. The key function should be set to sort by the second element of each tuple (the sum), which is achieved using `key=lambda x: x[1]`.
- Initialize an empty list `sorted_matrix` to store the sorted matrix.
- Using a for loop, iterate through each tuple in the sorted list of tuples. For each tuple, append the row (not including the sum) to the `sorted_matrix`.
- Return the `sorted_matrix`.
"""

E:
"""
Here are some examples to test the program:

- sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]) returns [[1, 1, 1], [1, 2, 3], [2, 4, 5]]
- sort_matrix([[5, 7, 8], [3, 2, 1], [6, 9, 4]]) returns [[3, 2, 1], [6, 9, 4], [5, 7, 8]]
- sort_matrix([[2, 3, 4], [1, 1, 1], [5, 6, 7]]) returns [[1, 1, 1], [5, 6, 7], [2, 3, 4]]
"""

def sort_matrix(matrix):
    sums