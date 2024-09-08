
def even_position(lst):
    return all(x % 2 == 0 for x in lst[::2])

print(even_position([3,2,1])) # False
"""
The function even_position checks every even index of a given list.
The [::2] slice is used to get every second element, which are the even indices.
The all function returns True if all elements in the iterable (the generator expression here) are True.
If any element is odd, the function returns False.
"""
<jupyter_output>
False
<jupyter_text>
Question 2
<jupyter_code>
