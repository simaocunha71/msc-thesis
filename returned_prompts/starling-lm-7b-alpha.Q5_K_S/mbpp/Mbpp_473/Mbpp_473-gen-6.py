
def tuple_intersection(tups, tups2):
    intersection = set(tups).intersection(tups2)
    return [list(tup) for tup in intersection]


