def index_minimum(lst):
    min_val = (None, None)
    min_val_index = 0
    for i, t in enumerate(lst):
        if t[1] < min_val[1]:
            min_val = t
            min_val_index = i
    return min_val[0]