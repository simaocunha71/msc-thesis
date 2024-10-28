```
def sort_matrix(matrix):
    return [list(t) for t in sorted(zip(*[iter(matrix)]*len(matrix[0])))]
```


This problem asks you to write a function that sorts a given matrix in ascending order according to the sum of its rows. The unit test `assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]` suggests that the function should return a new matrix with the same elements but sorted in ascending order by the sum of the rows.

Here's a Python solution for this problem:

```python
def sort_matrix(matrix):
    return [list(t) for t in sorted(zip(*[iter(matrix)]*len(matrix[0])))]
```

This function uses the built-in `zip` function to transpose the matrix, then uses the `sorted` function to sort the transposed matrix by the sum of its rows. The `iter` function is used to repeat the input matrix to the `zip` function the same number of times as the number of columns in the matrix. The `list` function is used to convert the tuples returned by the `zip` function back into lists. The `sorted` function returns a list of tuples, so the `list` function is used again to convert these tuples back into lists. The result is a new matrix with the same elements as the input matrix but sorted in ascending order by the sum of its rows. 





This function works by first transposing the matrix using the `zip` function. The `zip` function takes iterables (can be zero or more), aggregates them in a tuple, and returns it. The `*` operator is used to unpack the `matrix` into separate arguments to the `zip` function. The `iter` function is used to repeat the `matrix` the same number of times as the number of columns in the matrix. This is done to ensure that each row of the matrix is paired with each column.

After transposing the matrix, the function uses the `sorted` function to sort the transposed matrix. The `sorted` function takes an iterable and returns a new sorted list from the elements of the iterable. By default, the `sorted` function sorts the elements in ascending order.

The `sorted` function returns a list of tuples, where each tuple is a