def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]

print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]))


# Output: [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

"""
Explanation:
In the function, I use a list comprehension to iterate over each sublist in the given list and sort each one. The sorted function returns a new list containing all items from the original sublist in ascending order. I then return the new list.
"""
<jupyter_output>
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
<jupyter_text>
Question 3
<jupyter_code>
