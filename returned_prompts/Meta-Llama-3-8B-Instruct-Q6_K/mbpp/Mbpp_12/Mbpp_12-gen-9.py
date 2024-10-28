```
def sort_matrix(matrix):
    return [list(i) for i in sorted([[sum(row), row] for row in matrix])]
```


The problem asks to write a function that sorts a given matrix in ascending order according to the sum of its rows. The function should return the sorted matrix.

The unit test provided helps to clarify the problem. It shows that the function should return the matrix sorted by the sum of its rows, which is the sum of the elements in each row.

Here is the solution:

The solution uses list comprehension to create a list of lists, where each inner list contains the sum of the elements in a row and the row itself. The `sorted` function is then used to sort this list of lists based on the sum of the elements in each row. Finally, the function returns the sorted list of lists, which is the sorted matrix.

For example, if the input matrix is `[[1, 2, 3], [2, 4, 5], [1, 1, 1]]`, the function will first create a list of lists like this: `[[6, [1, 2, 3]], [7, [2, 4, 5]], [3, [1, 1, 1]]]`. Then, it will sort this list based on the sum of the elements in each row, resulting in `[[3, [1, 1, 1]], [6, [1, 2, 3]], [7, [2, 4, 5]]]`. Finally, it will return the sorted list of lists, which is the sorted matrix.