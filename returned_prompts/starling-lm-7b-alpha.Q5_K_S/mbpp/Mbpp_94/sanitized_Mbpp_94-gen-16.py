def index_minimum(tuple_list: list):
    return min(tuple_list, key=lambda x: x[1])[0]