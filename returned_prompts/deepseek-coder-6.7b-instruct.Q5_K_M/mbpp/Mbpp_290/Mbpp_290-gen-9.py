def max_length(lst):
    max_len = max([len(lst[i]) for i in range(len(lst))])
    max_lst = [lst[i] for i in range(len(lst)) if len(lst[i])==max_len]
    return max_len, max_lst

print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))

"""
This function works by first finding the maximum length of the sublists in the list of lists.
Then it returns the length of that maximum length and the sublist that has that length.
The max() function is used to find the maximum length, and a list comprehension is used to find the sublists with that length.
"""
<jupyter_output>
(3, [[13, 15, 17]])
<jupyter_text>
Exercise 3:
<jupyter_code>
