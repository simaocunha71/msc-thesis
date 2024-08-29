
def rotate_right(lst,n):
    return lst[-n:] + lst[:-n]

print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],3))

"""
Explanation:
In this function, we are slicing the given list from the end to the number of items we want to rotate (n), 
and from the start to the number of items we want to rotate (n). We then concatenate these two lists in reverse order 
to get the rotated list.
"""
<jupyter_output>
[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
<jupyter_text>
Question 2:
<jupyter_code>
