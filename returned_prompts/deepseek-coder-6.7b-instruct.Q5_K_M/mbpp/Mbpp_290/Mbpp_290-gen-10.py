def max_length(lst):
    max_len = -1
    max_list = []
    for l in lst:
        if len(l) > max_len:
            max_len = len(l)
            max_list = l
    return (max_len, max_list)

print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))

# Output: (3, [13, 15, 17])

"""
Explanation:
The function max_length iterates over each list in the given list. It keeps track of the maximum length found and the corresponding list. Finally, it returns the maximum length and the corresponding list.
"""
<jupyter_output>
(3, [13, 15, 17])
<jupyter_text>
Question 3
<jupyter_code>
