
def sum_range_list(lst, start, end):
    return sum(lst[start:end+1])

print(sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10))

"""
Here, lst[start:end+1] is used to slice the list from start index till end index (end inclusive). Then, sum() is used to find the sum of these elements.
"""
<jupyter_output>
29
<jupyter_text>
