
def Find_Max_Length(list_):
    max_length = 0
    for sublist in list_:
        if len(sublist) > max_length:
            max_length = len(sublist)
    return max_length

assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4

"""
Explanation:

The function Find_Max_Length takes a list of sublists as input. It initializes a variable max_length to 0.

Then it goes through each sublist in the input list. If the length of the current sublist is greater than max_length, it updates max_length with the length of the current sublist.

Finally, it returns the value of max_length, which holds the length of the longest sublist.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
