def sort_matrix(m):
    return sorted(m, key=sum)

print(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]))

# Output: [[1, 1, 1], [1, 2, 3], [2, 4, 5]]

"""
In the function sort_matrix, we use the built-in sorted function, along with the key parameter. The key parameter is a function that takes an element and returns a value that will be used for sorting purposes. In this case, we use the built-in sum function as the key, which will sort the elements in the matrix based on the sum of their rows.
"""
<jupyter_output>
[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
<jupyter_text>
Q2:
<jupyter_code>
"""
Given a list of tuples where each tuple contains two integers, write a Python program to sort the list in ascending order by the sum of the numbers in each tuple.

For example, if the input is [(4, 5), (2, 3), (9, 1)], the output should be [(9, 1), (2, 3), (4, 5)].
"""

def sort_tuples(lst):
    return sorted(lst, key=sum)

print(sort_tuples([(4, 5), (2, 3), (9, 1)]))

# Output: [(9, 1), (2, 3), (4, 5)]

"""
In the function sort_tuples, we use the built-in sorted function, along with the key parameter. The key parameter is a function that takes an element and returns a value that will be used for sorting purposes. In this case, we use the built-in sum function as the key, which will sort the elements in the list based on the sum of their numbers.
"""
<jupyter_output>
[(9, 1), (2, 3), (4, 5)]