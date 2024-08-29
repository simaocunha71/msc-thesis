
def Find_Max(lst):
    max_len = -1
    max_element = []
    for i in lst:
        if len(i) > max_len:
            max_len = len(i)
            max_element = i
    return max_element

print(Find_Max([['A'],['A','B'],['A','B','C']]))

#Output: ['A','B','C']

"""
Explanation:
In the given list, the sub-lists are ['A'], ['A','B'], ['A','B','C'].
The length of each sub-list is calculated using the len() function.
The sub-list ['A','B','C'] has the maximum length which is 3.
So, the function returns the sub-list ['A','B','C'].
"""
<jupyter_output>
['A', 'B', 'C']
<jupyter_text>
2. Write a python function to find the element of a list having minimum length.
<jupyter_code>
