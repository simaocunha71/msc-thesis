def unique_sublists(lst):
    return {tuple(sublist): lst.count(tuple(sublist)) for sublist in set(tuple(sub) for sub in lst)}