def index_minimum(list_of_tuples):
    minimum = float('inf')
    for i in list_of_tuples:
        if i[1] < minimum:
            minimum = i[1]
            minimum_index = i[0]
    return minimum_index