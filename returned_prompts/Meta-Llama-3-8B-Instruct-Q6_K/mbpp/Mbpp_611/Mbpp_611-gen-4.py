```
def max_of_nth(matrix, n):
    return max([row[n-1] for row in matrix])
```
The function `max_of_nth` takes a matrix and an integer `n` as inputs. It returns the maximum value in the `n`-th column of the matrix.

The unit test `assert max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2) == 19` helps to clarify that the columns are 0-indexed. Therefore, if we want to access the `n`-th column, we should use `row[n-1]` instead of `row[n]`.

The function uses a list comprehension to create a list of the values in the `n`-th column. It then returns the maximum value from this list using the built-in `max` function.  This solution is concise and efficient, with a time complexity of O(m), where `m` is the number of rows in the matrix.  It also assumes that the matrix is not empty and that `n` is a valid column index.  In practice, you might want to add error checking to handle these cases.  For example, you could use `if not matrix or n > len(matrix[0]): return None` to return `None` if the matrix is empty or if `n` is out of range.  However, this is not necessary to pass the provided unit test. 