```
def max_of_nth(matrix, n):
    return max([row[n] for row in matrix])
```




Test:
```
assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19
```




Explanation: 
The function `max_of_nth` takes a matrix represented as a list of lists and an integer `n` as input. It returns the maximum value in the `n'th` column of the matrix. The `n'th` column is accessed by indexing each row with `n`. The maximum of these values is found using the built-in `max` function. The result is returned as the output of the function. 

The unit test provided, `assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19`, ensures that the function is working correctly by comparing the output of the function with the expected output. If the function is working correctly, the test will pass, otherwise, it will fail. 

This solution has a time complexity of O(m), where m is the number of rows in the matrix, because it needs to iterate over each row once to access the `n'th` column. The space complexity is O(m), because it needs to store the values of the `n'th` column in a list before finding the maximum. 