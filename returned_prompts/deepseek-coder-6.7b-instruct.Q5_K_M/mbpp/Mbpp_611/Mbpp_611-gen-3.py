
def max_of_nth(matrix, n):
    return max(row[n] for row in matrix)

print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2)) # 19

# Alternative solution using list comprehension
def max_of_nth(matrix, n):
    return max([row[n] for row in matrix])

print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2)) # 19

# Alternative solution using numpy
import numpy as np

def max_of_nth(matrix, n):
    return np.array(matrix).T[n].max()

print(max_of_nth([[5, 6, 7], [1, 3, 5], [8, 9, 19]], 2)) # 19
<jupyter_output>
19
19
19
<jupyter_text>
Exercise 4: List of lists sorting
<jupyter_code>
