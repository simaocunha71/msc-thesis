```
def max_of_nth(matrix, n):
    return max([row[n] for row in matrix])
```
This function takes a matrix (a list of lists) and an integer `n` as input, and returns the maximum value in the `n`-th column of the matrix.

The unit test `assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19` helps to clarify the problem by providing an example of a valid input and the expected output.

The solution uses a list comprehension to extract the `n`-th element of each row in the matrix, and then uses the built-in `max` function to find the maximum of these elements. This approach is efficient and easy to understand.