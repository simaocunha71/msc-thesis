```
def sort_matrix(matrix):
    return [list(i) for i in sorted(((sum(row), row) for row in matrix), key=lambda x: x[0])]
```





This function sorts the matrix in ascending order according to the sum of its rows. It uses a lambda function as the key for the built-in sorted function. The sorted function returns a list of tuples, where each tuple contains the sum of a row and the row itself. The lambda function is used to specify that the sorting should be done based on the sum of the rows. The function then converts the list of tuples back into a list of lists, with each list being a row in the original matrix.

For example, if the input is `[[1, 2, 3], [2, 4, 5], [1, 1, 1]]`, the output will be `[[1, 1, 1], [1, 2, 3], [2, 4, 5]]`, which is the input matrix sorted in ascending order according to the sum of its rows.