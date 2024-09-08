def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]

print(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]))

"""
This function uses a list comprehension to create a new list of sorted sublists. The sorted function is used to sort each sublist.
"""
<jupyter_output>
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
<jupyter_text>
