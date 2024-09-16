def index_minimum(lst):
    if not lst:
        return None
    minimum = lst[0][1]
    index = 0
    for i, (_, v) in enumerate(lst):
        if v < minimum:
            minimum = v
            index = i
    return lst[index][0]
