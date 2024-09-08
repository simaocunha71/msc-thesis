def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]

print(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]))

#Output: [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

"""
Explanation:
The function sort_sublists takes a list of lists as input.
It uses a list comprehension to create a new list.
In the list comprehension, for each sublist in the input list, it applies the sorted() function which returns a new list containing all items from the original list in ascending order.
The resulting list of sorted sublists is returned by the function.
"""
<jupyter_output>
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
<jupyter_text>
Question 5:Write a function that takes a string and returns the number of unique words in the string.
<jupyter_code>
