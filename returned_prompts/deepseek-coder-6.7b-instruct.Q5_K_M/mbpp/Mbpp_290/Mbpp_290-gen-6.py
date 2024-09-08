
def max_length(lst):
    max_len = 0
    max_lst = []
    for sub_lst in lst:
        if len(sub_lst) > max_len:
            max_len = len(sub_lst)
            max_lst = sub_lst
    return (max_len, max_lst)

print(max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))

# Output: (3, [13, 15, 17])
<jupyter_output>
(3, [13, 15, 17])
<jupyter_text>
Question 3
<jupyter_code>
