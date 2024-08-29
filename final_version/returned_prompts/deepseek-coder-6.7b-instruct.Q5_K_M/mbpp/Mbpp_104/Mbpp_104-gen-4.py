def sort_sublists(lst):
    for i in range(len(lst)):
        lst[i] = sorted(lst[i])
    return lst

print(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]))

"""
Output:
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
"""

# Q2
