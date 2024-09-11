```
def max_of_nth(matrix, n):
    assert type(matrix) == list and type(n) == int
    if n >= len(matrix[0]):
        return None
    res = []
    for i in matrix:
        res.append(i[n])
    return max(res)
```

Explanation:

The function `max_of_nth` takes a matrix and a column number as arguments. It first checks if the matrix is a list and if the column number is an integer. If not, it raises an error.

Then, it initializes an empty list called `res` to store the values of the nth column of the matrix. 

Next, it iterates over each row in the matrix and appends the value of the nth column to the `res` list. 

Finally, it returns the maximum value in the `res` list.

This function can be used to find the maximum value of the nth column in a matrix.

For example, if we call `max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2)`, it will return 19, which is the maximum value of the second column in the matrix `[[5, 6, 7], [1, 3, 5], [8, 9, 19]]`.

Note that if the column number is greater than or equal to the number of columns in the matrix, the function will return None.

Overall, this function provides a straightforward way to find the maximum value of a specific column in a matrix.

Here's a step-by-step breakdown of the code:

1. Check if the matrix and column number are of the correct type and format. If not, raise an error.
2. Initialize an empty list called `res` to store the values of the nth column of the matrix.
3. Iterate over each row in the matrix.
4. For each row, append the value of the nth column to the `res` list.
5. Return the maximum value in the `res` list.

This function can be used to find the maximum value of the nth column in a