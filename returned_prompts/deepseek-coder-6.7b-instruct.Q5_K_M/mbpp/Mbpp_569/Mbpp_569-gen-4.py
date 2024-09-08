def sort_sublists(lst):
    result = []
    for sublist in lst:
        result.append(sorted(sublist))
    return result

print(sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]))


