def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]

print(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]))

# OUTPUT: [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

# This function uses a list comprehension to iterate over each sublist in the given list of lists. The sorted function is used to sort each sublist, and the results are collected into a new list which is then returned.
<jupyter_output>
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
<jupyter_text>
Question 7
<jupyter_code>
