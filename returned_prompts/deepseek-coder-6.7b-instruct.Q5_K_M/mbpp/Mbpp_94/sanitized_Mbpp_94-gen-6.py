def index_minimum(lst):
    lst.sort(key=lambda x: x[1])
    return lst[0][0]