```
def sort_matrix(matrix):
    return sorted(matrix, key=lambda x: sum(x))
```


The problem asks to write a function that sorts a given matrix in ascending order according to the sum of its rows. 

The unit test provided, `assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]`, helps to understand the problem better. It shows that the function should return a new matrix with the same elements, but in a different order.

To solve this problem, we can use the built-in `sorted` function in Python, along with a lambda function as the key. The lambda function calculates the sum of each row, and the `sorted` function sorts the matrix based on these sums. The `sorted` function returns a new list, so we can assign this to the original variable to overwrite the original matrix. 

Here is the solution:

```
def sort_matrix(matrix):
    return sorted(matrix, key=lambda x: sum(x))
```

This function takes a matrix as input, calculates the sum of each row using the lambda function, and sorts the matrix based on these sums. The sorted matrix is then returned. 

When you run this function with the provided unit test, it will return the expected result: `[[1, 1, 1], [1, 2, 3], [2, 4, 5]]`. 

This solution assumes that the input matrix is a list of lists, where each inner list represents a row in the matrix. It also assumes that the matrix is not empty. If the matrix is empty, the function will return an empty list. If the matrix is not a list of lists, the function may not work correctly. 

In terms of time complexity, the function has a time complexity of O(n log n), where n is the number of rows in the matrix. This is because the `sorted` function has a time complexity of O(n log n) in the worst case, and it is called once on the matrix. The lambda function has a constant time complexity, so it does not affect the overall time complexity. 

In terms of space complexity, the function has a space complexity of O(n), where n is the number of rows in the matrix. This is because the `sorted` function returns a new list,