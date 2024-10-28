def unique_sublists(lst):
    return {tuple(sublist): lst.count(tuple(sublist)) for sublist in set(tuple(sublist) for sublist in lst)}