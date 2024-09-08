def swap_List(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

print(swap_List([12, 35, 9, 56, 24]))

"""
Explanation:
The function swap_List takes a list as an argument. It uses the Python list slicing feature to interchange the first and last elements. The elements at positions 0 and -1 in the list (which are the first and last elements) are swapped. The new list is returned.
"""
<jupyter_output>
[24, 35, 9, 56, 12]
<jupyter_text>
4. Write a Python function to find a tuple, within a list of tuples, with the largest last element.
<jupyter_code>
