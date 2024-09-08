def split_two_parts(lst, L):
    return (lst[:L], lst[L:])

print(split_two_parts([1,1,2,3,4,4,5,1],3))

# Output: ([1, 1, 2], [3, 4, 4, 5, 1])

"""
Explanation:
The function `split_two_parts` takes in a list and an integer L. 
It returns a tuple containing two lists. 
The first list is obtained by slicing the input list from the start to the index L. 
The second list is obtained by slicing the input list from the index L to the end.
"""
<jupyter_output>
([1, 1, 2], [3, 4, 4, 5, 1])
<jupyter_text>
Q2:
<jupyter_code>
