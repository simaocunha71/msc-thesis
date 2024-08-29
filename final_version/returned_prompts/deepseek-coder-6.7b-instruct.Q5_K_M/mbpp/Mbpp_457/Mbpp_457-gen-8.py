
def Find_Min(lst):
    min_len = min([len(sublist) for sublist in lst])
    for sublist in lst:
        if len(sublist) == min_len:
            return sublist

print(Find_Min([[1],[1,2],[1,2,3]]))

"""
Output:
[1]
"""

Explanation:
The function Find_Min takes a list of lists as input, finds the length of the smallest sublist, then returns the sublist of the same minimum length.
<jupyter_output>
<empty_output>
<jupyter_text>
