def sort_sublists(lst):
    return [sorted(sublist) for sublist in lst]

print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]))  # Output: [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]


