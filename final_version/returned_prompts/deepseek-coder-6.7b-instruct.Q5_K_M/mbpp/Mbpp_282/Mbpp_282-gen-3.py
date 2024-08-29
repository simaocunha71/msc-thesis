def sub_list(l1, l2):
    return [a - b for a, b in zip(l1, l2)]

print(sub_list([1, 2, 3],[4,5,6]))

# Output: [-3, -3, -3]

# Explanation:
# The function sub_list subtracts corresponding elements from l1 and l2.
# The zip function is used to combine l1 and l2 into pairs of elements. The list comprehension then subtracts these pairs.

# Solution by:
# https://github.com/rkansal27
<jupyter_output>
[-3, -3, -3]
<jupyter_text>
Problem 4
<jupyter_code>
