def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]

print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]))

# Output: [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

"""
This function uses a list comprehension to iterate over each sublist in the given list. The sorted function is used to sort each sublist, and the results are collected into a new list.
"""

"""
Alternatively, you could use a for loop to achieve the same result:

def sort_sublists(lst):
    result = []
    for sublist in lst:
        result.append(sorted(sublist))
    return result

print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]))
"""

"""
Both of these functions will return the same result. The list comprehension version is more concise and readable.
"""
<jupyter_output>
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
<jupyter_text>
