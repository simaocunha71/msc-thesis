def index_minimum(my_list):
    return min(my_list, key=lambda tup: tup[1])[0]