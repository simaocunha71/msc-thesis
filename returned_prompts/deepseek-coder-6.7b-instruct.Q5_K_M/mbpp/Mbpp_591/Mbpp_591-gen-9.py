def swap_List(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
"""
The function works by using tuple unpacking to swap the first and last elements of the list. The time complexity of this function is O(1), meaning it performs a constant number of operations regardless of the size of the input list.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3
<jupyter_code>
