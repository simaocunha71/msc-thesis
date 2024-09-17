```
def max_of_nth(matrix, n):
    return max([row[n] for row in matrix])
```


This function works by iterating over each row in the matrix and selecting the nth element of each row. It then returns the maximum of these elements. The unit test provided shows that this function should return 19 for the given matrix and nth column (2). 

The unit test also shows that the function should return the maximum of the n'th column, not the maximum of the row. This is why we are selecting the nth element of each row, rather than returning the maximum of the entire row. 

The function also assumes that the matrix is not empty and that n is a valid column index (i.e., 0 <= n < len(matrix[0])). If the matrix is empty or n is not a valid column index, the function will raise an exception. 

If we want to handle these cases, we can add some error checking code. For example, we could check if the matrix is empty before trying to access its elements, and we could check if n is a valid column index before trying to access the nth element of each row. 

Here is an example of how we could add this error checking code:
```
def max_of_nth(matrix, n):
    if not matrix:
        return None
    if n < 0 or n >= len(matrix[0]):
        return None
    return max([row[n] for row in matrix])
```
This version of the function will return None if the matrix is empty or if n is not a valid column index, rather than raising an exception. 
```
```


