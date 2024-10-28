def index_minimum(lst):
    min_second_value = min(lst, key=lambda x: x[1])[1]
    for tup in lst:
        if tup[1] == min_second_value:
            return tup[0]