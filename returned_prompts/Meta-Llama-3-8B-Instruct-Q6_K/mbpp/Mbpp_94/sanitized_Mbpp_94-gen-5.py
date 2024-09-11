def index_minimum(lst):
    min_val = min(lst, key=lambda x: x[1])
    return min_val[0]  # returns the first element of the tuple with the smallest second value