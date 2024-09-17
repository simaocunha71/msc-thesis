```
def sort_matrix(matrix):
    matrix.sort(key=sum)
    return matrix
```


This function uses Python's built-in sort function, which sorts the list in-place. The key argument is a function that takes a row of the matrix and returns a value that will be used for sorting purposes. In this case, the function is sum, which adds up the elements in a row and returns the total. The sort function uses these values to sort the rows of the matrix. The sorted matrix is then returned. 

For example, if we call `sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])`, it will return `[[1, 1, 1], [1, 2, 3], [2, 4, 5]]`, which is the original matrix sorted in ascending order according to the sum of its rows. 

The unit test `assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]` ensures that the function is working correctly. 

The time complexity of this function is O(n log n), where n is the number of rows in the matrix. This is because the sort function has a time complexity of O(n log n) in the worst case. The space complexity is O(1), because we are not using any additional space that scales with the input size. 