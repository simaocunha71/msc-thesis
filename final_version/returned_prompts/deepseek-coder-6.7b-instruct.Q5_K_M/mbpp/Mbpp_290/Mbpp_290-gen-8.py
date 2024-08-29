def max_length(lst):
    max_len = 0
    max_lst = []
    for sub_lst in lst:
        if len(sub_lst) > max_len:
            max_len = len(sub_lst)
            max_lst = sub_lst
    return (max_len, max_lst)

print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))

"""
Output:
(3, [13, 15, 17])
"""

# Answer:

# The function max_length takes in a list of lists and then iterates through the list to find the list that has the highest length. 
# It then returns this highest length along with the list itself.

# The built-in function len() is used to determine the length of each sub-list. The variable max_len is used to keep track of the highest length found so far. 
# If a sub-list has a length greater than max_len, max_len is updated and max_lst is updated to be the sub-list. 
# Finally, max_len and max_lst are returned as a tuple.
<jupyter_output>
(3, [13, 15, 17])
<jupyter_text>
Question 2:
<jupyter_code>
