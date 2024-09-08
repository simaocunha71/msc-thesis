def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]

print(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]))

"""
The function sort_sublists takes a list of lists as input. It uses a list comprehension to create a new list where each sublist is sorted. The sorted function is used to sort each sublist. The sorted sublists are then returned as the output of the function.
"""

#Question 2
