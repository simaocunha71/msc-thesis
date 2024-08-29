
def Find_Min_Length(lst):
    return min(len(lst) for lst in lst)

print(Find_Min_Length([[1],[1,2]]))

"""
Explanation:
This function works by using a generator expression to get the lengths of all the inner lists, and then uses the min function to get the smallest of these lengths. The result is the length of the smallest list in the input list of lists.
"""
<jupyter_output>
1
<jupyter_text>
Question 2
<jupyter_code>
"""
