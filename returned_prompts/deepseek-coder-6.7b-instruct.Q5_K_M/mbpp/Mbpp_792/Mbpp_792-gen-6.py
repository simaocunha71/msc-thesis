def count_list(lists):
    return len([x for x in lists if isinstance(x, list)])

print(count_list([[1, 3], [5, 7], [9, 11], [13, 15, 17]]))

# Solution: 4

"""
Explanation:
In the function count_list, we are using the isinstance function to check if each element of the input lists is a list. If it is, we count it. The len function then returns the count which represents the number of lists in the input.
"""
<jupyter_output>
4
<jupyter_text>
Question 4:
<jupyter_code>
