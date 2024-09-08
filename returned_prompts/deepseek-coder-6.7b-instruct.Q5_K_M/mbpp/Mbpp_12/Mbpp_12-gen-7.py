def sort_matrix(matrix):
    return sorted(matrix, key=sum)

print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))

# OUTPUT: [[1, 1, 1], [1, 2, 3], [2, 4, 5]]

Explanation:

In the function `sort_matrix`, we use the `sorted` function to sort the rows of the matrix. The `key` parameter is set to `sum`, so the rows are sorted based on the sum of their elements.

This works because the `sum` function is callable and returns the sum of elements of a list. When `sorted` compares two rows, it computes the sum of elements for each and sorts the rows accordingly.

This solution has a time complexity of O(m*n*log(m)), where m is the number of rows and n is the number of columns in the matrix. This is because for each row, we compute the sum (which takes O(n) time), and we do this for m rows, so we have O(m*n) time in total. Then we sort these m sums, which takes O(log(m)) time.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
"""
