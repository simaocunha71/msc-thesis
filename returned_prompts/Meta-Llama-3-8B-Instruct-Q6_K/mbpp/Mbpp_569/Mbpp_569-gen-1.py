def sort_sublists(list_of_lists):
    return [sorted(sublist) for sublist in list_of_lists]

# Test the function
print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])) # [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]







