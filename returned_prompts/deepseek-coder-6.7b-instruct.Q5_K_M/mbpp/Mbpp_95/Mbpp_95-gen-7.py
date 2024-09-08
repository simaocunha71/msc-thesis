
def Find_Min_Length(lst):
    return min(len(sublist) for sublist in lst)

assert Find_Min_Length([[1],[1,2]]) == 1
"""
Explanation:
This function works by using a generator expression to create a sequence of length values. Then it uses the built-in min function to find the smallest length in the sequence.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
