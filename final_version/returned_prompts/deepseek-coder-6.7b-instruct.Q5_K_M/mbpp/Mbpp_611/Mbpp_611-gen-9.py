
def max_of_nth(matrix, n):
    return max(row[n] for row in matrix)

# test
print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2))  # expected output: 19

# Explanation:
# The function `max_of_nth` takes a matrix and a column number `n` as input. It uses a generator expression `row[n] for row in matrix` to create a sequence of the n'th elements of the rows, and `max` function to find the maximum of these elements.
# In the given example, the function will return the max of the 2nd column, which is 19.
<jupyter_output>
19
<jupyter_text>
Exercise 2.1.8: List of lists (2)
<jupyter_code>
