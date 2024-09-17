```
def max_of_nth(matrix, n):
    return max([row[n] for row in matrix])
```
This function uses a list comprehension to create a list of the n'th elements of each row in the matrix, and then returns the maximum of that list. The unit test provided ensures that the function works correctly. For example, `max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2)` should return `19`, which is the maximum of the second column in the given matrix. 

The function can be used to find the maximum of any column in the matrix, not just the last one. The column is specified by the value of `n`, which is a zero-based index. For example, `max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 0)` would find the maximum of the first column, which is `8`. 

The function is case-insensitive, so it would work correctly even if the matrix contains negative numbers or non-integer values. It also works correctly if the matrix is empty or if the specified column does not exist (in which case it would raise an `IndexError`). However, it is the responsibility of the caller to ensure that the matrix is not empty and that `n` is a valid column index. 

The time complexity of this function is O(m), where `m` is the number of rows in the matrix, because it needs to iterate over each row once. The space complexity is O(m), because it needs to store the n'th elements of each row in a list.  However, the space complexity could be improved to O(1) by using a variable to keep track of the maximum value, rather than a list. This would make the function more efficient for large matrices, but it would also make it less flexible and more difficult to use. 