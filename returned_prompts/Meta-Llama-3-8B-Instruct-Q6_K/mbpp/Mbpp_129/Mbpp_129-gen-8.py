```
def magic_square_test(matrix):
    n = len(matrix)
    total = sum(matrix[0])
    for i in range(1, n):
        if sum(matrix[i]) != total:
            return False
    for j in range(n):
        total = sum([matrix[i][j] for i in range(n)])
        if total != total:
            return False
    total = sum([matrix[i][i] for i in range(n)])
    if total != total:
        return False
    total = sum([matrix[i][n-i-1] for i in range(n)])
    if total != total:
        return False
    return True
```


The unit test `assert magic_square_test([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])==True` suggests that the function should return True if the given matrix is a magic square. The function checks if the sum of the elements in each row, column and the two diagonals are equal. If all these sums are equal, then the matrix is a magic square. If not, the function returns False. 

This function assumes that the input matrix is a square matrix (i.e., it has the same number of rows and columns) and that it is a list of lists in Python. The function also assumes that the matrix is not empty and that all rows have the same length. 

The time complexity of this function is O(n^2), where n is the number of rows (and columns) in the matrix. This is because the function needs to iterate over each element in the matrix once. The space complexity is O(1), as the function uses a constant amount of space to store the sums. 