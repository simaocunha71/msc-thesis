```
def max_of_nth(matrix, n):
    return max([row[n] for row in matrix])
```


This function uses list comprehension to create a list of the nth elements from each row in the matrix, and then uses the built-in max function to find the maximum of those elements. The unit test provided ensures that this function works correctly by checking that it returns the maximum of the third column of the given matrix.