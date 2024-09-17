def index_minimum(tuples):
    min_val = tuples[0]
    for t in tuples:
        if t[1] < min_val[1]:
            min_val = t
    return min_val[0]