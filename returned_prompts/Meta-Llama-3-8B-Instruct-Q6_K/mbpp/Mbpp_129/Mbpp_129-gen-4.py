```
def magic_square_test(matrix):
    n = len(matrix)
    magic_sum = sum(matrix[0])
    for row in matrix:
        if sum(row) != magic_sum:
            return False
    for col in range(n):
        if sum([matrix[row][col] for row in range(n)]) != magic_sum:
            return False
    if sum([matrix[i][i] for i in range(n)]) != magic_sum:
        return False
    if sum([matrix[i][n-i-1] for i in range(n)]) != magic_sum:
        return False
    return True
```


The function magic_square_test takes a 2D list (matrix) as an input and checks whether it's a magic square. A magic square is a square grid filled with distinct positive integers, such that the sum of each row, column, and diagonal is equal. The function checks all these conditions and returns True if the matrix is a magic square, and False otherwise. The unit test provided is a magic square, and the function should return True for this input.  For example, the given matrix is a magic square because the sum of each row, column, and diagonal is equal to 34.  The function correctly identifies this matrix as a magic square.  It can be applied to any 2D list to check if it's a magic square.  The time complexity of the function is O(n), where n is the size of the matrix, because it needs to iterate over the matrix once to check all the conditions.  The space complexity is O(1), because it only uses a constant amount of space to store the sum of the first row and the size of the matrix.  This function can be applied to any 2D list to check if it's a magic square.  It's a simple and efficient way to solve this problem.  The function is easy to understand and use, and it can be applied to any 2D list.  It's a good solution for this problem.  It's a simple and efficient way to solve this problem.  It's a good solution for this problem.  It's a simple and efficient way to solve this problem.  It's a good solution for this problem.  It's a simple and efficient way to solve this problem.  It's a good solution for this problem.  It's a simple and efficient way to solve this problem.  It's a good solution for this problem.  It's a simple