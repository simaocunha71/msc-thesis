```
def max_of_nth(matrix, n):
    return max(row[n] for row in matrix)
```
This function uses a generator expression to iterate over each row in the matrix, and then selects the nth element of each row using row[n]. The max function is then used to find the maximum of these elements. 

The unit test `assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19` ensures that the function works correctly. It checks that the function returns 19, which is the maximum of the third column in the given matrix. 