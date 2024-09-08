def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]

print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]))

# OUTPUT: [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

"""
In the above code, we are using list comprehension to go through each sublist in the list of lists. The sorted function is used to sort the elements in each sublist.
"""
<jupyter_output>
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
<jupyter_text>
Question 3:
<jupyter_code>
