def index_minimum(my_list):
    smallest = min(my_list, key=lambda x: x[1])
    return smallest[0]