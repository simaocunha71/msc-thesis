def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]

print(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]))

"""
Output:
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""

# Explanation:
# This function uses list comprehension to create a new list. For each sublist in the original list, it sorts the sublist and adds it to the new list. The sorted function is used to sort the elements of each sublist. The sorted sublists are then returned as a new list.
<jupyter_output>
<empty_output>
<jupyter_text>
