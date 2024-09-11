def sort_sublists(lists):
    """
    Arguments:
        lists -- a list of lists
    Returns:
        a list of sorted sublists
    """
    for sublist in lists:
        sublist.sort()
    return lists


# Run tests
print(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]))
# Expected output: [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
print(sort_sublists([["red", "blue", "green"], ["white", "black", "orange"]]))
# Expected output: [['blue', 'green', 'red'], ['black', 'orange', 'white']]
print(sort_sublists([["blue", "green", "red"], ["white", "black", "orange"]]))
# Expected output: [['blue', 'green', 'red'], ['black', 'orange', 'white']]
print(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]))
# Expected output: [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
print(sort_sublists([["green", "orange"], ["white", "black"], ["white", "black", "orange"]]))
# Expected output: [['green', 'orange'], ['black', 'white', 'white'], ['black', 'white', 'orange']]
print(sort_sublists([["green", "orange"], ["white", "black", "white"]]))
# Expected output: [['green', 'orange'], ['black', 'white', 'white']]
print(sort_sublists([["green"], ["orange"], ["white"], ["black"], ["white", "black"]]))
# Expected output: [['green'], ['orange'], ['black', 'white'], ['white']]
```

This function `sort_sublists` takes a list of lists as an argument and sorts each sublist of strings in the given list of lists. It uses a for loop to iterate through each