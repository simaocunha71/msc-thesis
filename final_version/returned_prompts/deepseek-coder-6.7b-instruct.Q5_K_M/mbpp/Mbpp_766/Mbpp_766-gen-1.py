
def pair_wise(lst):
    return [(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]

print(pair_wise([1,1,2,3,3,4,4,5]))

"""
The function `pair_wise` takes as input a list `lst` and returns a new list where each element is a pair of consecutive elements from `lst`.

In the return statement, we're using a list comprehension to generate the new list. For each index `i` in the range of the length of `lst` minus 1, we're creating a tuple of the element at index `i` and the element at index `i + 1`.
"""

# Output: [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
<jupyter_output>
[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
<jupyter_text>
Question 2
<jupyter_code>
