
def Find_Max_Length(lst):
    return max(len(sublist) for sublist in lst)

assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4
"""
The function works by using a generator expression to iterate over all sublists in the provided list, and then using the built-in max function to return the length of the longest sublist.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:
<jupyter_code>
