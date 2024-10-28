```
def sort_matrix(matrix):
    sorted_matrix = sorted(((sum(row), row) for row in matrix), key=lambda x: x[0])
    return [row[1] for row in sorted_matrix]
```


The provided unit test suggests that the matrix should be sorted in ascending order based on the sum of its rows. 

The function `sort_matrix` first calculates the sum of each row in the matrix. Then, it sorts the matrix based on these sums. The `sorted` function is used with a generator expression that calculates the sum of each row and returns a tuple containing the sum and the row. The `key` parameter is set to `lambda x: x[0]` to sort the matrix based on the sums.

Finally, the function returns a list of the sorted rows, obtained by extracting the second element of each tuple in the sorted list. 
This solution has a time complexity of O(m log m) where m is the number of rows in the matrix, as it involves sorting the matrix. 
The space complexity is O(m) as it needs to store the sorted matrix. 







# Test cases
assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]

assert sort_matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])==[[1, 2, 3], [1, 2, 3], [1, 2, 3]]

assert sort_matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])==[[1, 1, 1], [1, 1, 1], [1, 1, 1]]

assert sort_matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])==[[1, 1, 1], [2, 2, 2], [3, 3, 3]]

assert sort_matrix([])==[]

assert sort_matrix([[1]])==[[1]]

assert sort_matrix([[1, 2]])==[[1, 2]]

assert sort_matrix([[1, 2, 3], [4,