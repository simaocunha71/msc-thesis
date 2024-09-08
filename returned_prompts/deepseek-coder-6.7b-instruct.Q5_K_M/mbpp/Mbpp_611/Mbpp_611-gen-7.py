
def max_of_nth(matrix, n):
    return max(row[n] for row in matrix)

print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2))
<jupyter_output>
19
<jupyter_text>
12. Write a Python function to get the unique values from a list. Return the values in the same order they first appear in the provided list.
<jupyter_code>
