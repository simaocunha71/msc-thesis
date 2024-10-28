
def index_minimum(my_list):
    minimum = min(my_list, key=lambda x: x[1])
    return minimum[0]


