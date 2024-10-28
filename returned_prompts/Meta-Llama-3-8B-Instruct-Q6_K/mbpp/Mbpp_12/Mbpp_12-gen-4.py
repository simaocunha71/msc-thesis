```
def sort_matrix(matrix):
    return [i for _, i in sorted(((sum(row), row) for row in matrix))]
```







Solution:
```
def sort_matrix(matrix):
    return [i for _, i in sorted(((sum(row), row) for row in matrix))]
```







Explanation:
The task is to sort a given matrix in ascending order based on the sum of its rows. The unit test `assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]` provides an example of the expected output.

To solve this problem, we can use a list comprehension to iterate over each row in the matrix, calculate the sum of each row, and then sort the rows based on their sums. The sorted function returns a list of tuples, where each tuple contains the sum of the row and the row itself. The list comprehension then extracts the rows from these tuples.

Here is the implementation in Python:
```
def sort_matrix(matrix):
    return [i for _, i in sorted(((sum(row), row) for row in matrix))]
```
This function takes a matrix as input, calculates the sum of each row, sorts the rows based on their sums, and returns the sorted matrix. The unit test provided in the problem statement confirms that this function produces the expected output.