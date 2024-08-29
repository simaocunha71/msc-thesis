def count_X(tup, elem):
    return tup.count(elem)

print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 10))  # 2
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4))  # 0
print(count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 8))  # 3

"""
Explanation:
The function 'count_X' takes in a tuple and an element as input. It uses the built-in 'count' function to count the occurrences of the element in the tuple and returns the result.
"""
<jupyter_output>
2
0
3
<jupyter_text>
Q2. Write a Python function that takes in a list of tuples and returns a list of lists where each tuple has been converted into a list.
<jupyter_code>
# For example:
# input: [(1,2), (3,4), (5,6)]
# output: [[1,2], [3,4], [5,6]]
def convert_tuples(lst):
    return [list(i) for i in lst]

print(convert_tuples([(1,2), (3,4), (5,6)]))
<jupyter_output>
[[1, 2], [3, 4], [5, 6]]
<jupyter_text>
Q3. Write a Python function that takes in a list of strings and returns a list of strings where each string has been converted to uppercase.
<jupyter_code>
# For example:
# input: ['apple', 'banana', 'cherry']
# output: ['APPLE', 'BANANA', 'CHERRY