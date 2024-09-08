
def swap_List(lst):
    """Swap the first and last elements in a list."""
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# Testing
print(swap_List([12, 35, 9, 56, 24]))
<jupyter_output>
[24, 35, 9, 56, 12]
<jupyter_text>
Problem 4
<jupyter_code>
