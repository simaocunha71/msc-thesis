To solve this problem, we can first calculate the sum of each row in the matrix, and then sort the matrix based on these sums. Here is the Python code:

```python
def sort_matrix(matrix):
    rows = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
    row_sums = [sum(row) for row in rows]
    sorted_rows = sorted(rows, key=lambda row: row_sums.index(sum(row)))
    return [sorted_rows[i] for i in range(len(matrix))]

assert sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]])==[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
```

Here is a detailed explanation of the solution:

1. First, we calculate the sum of each row in the matrix, and store them in the `row_sums` list.
2. Then, we sort the rows of the matrix based on the `row_sums` list. Here, we use the `sorted` function to sort the list. The `key` parameter is a function that takes a row as input and returns the index of its sum in the `row_sums` list. This allows us to sort the rows based on the sums.
3. Finally, we return the sorted rows as the sorted matrix.

The time complexity of this solution is O(m * n + m * log(m)) and the space complexity is O(m + n), where m is the number of rows in the matrix and n is the number of columns in the matrix.

```python
def sort_matrix(matrix):
    rows = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
    row_sums = [sum(row) for row in rows]
    sorted_rows = sorted(rows, key=lambda row: row_sums.index(sum(row)))
    return [sorted_rows[i] for i in range(len(matrix))]
