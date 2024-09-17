def unique_sublists(lst):
    return {tuple(sublist): sublist.count(sublist) for sublist in lst}