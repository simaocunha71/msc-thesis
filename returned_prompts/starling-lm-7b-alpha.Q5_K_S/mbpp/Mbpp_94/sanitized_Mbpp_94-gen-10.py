def index_minimum(list_of_tuples):
    minimum_index = 0
    minimum_value = list_of_tuples[0][1]
    for index in range(len(list_of_tuples)):
        if list_of_tuples[index][1] < minimum_value:
            minimum_value = list_of_tuples[index][1]
            minimum_index = index
    return list_of_tuples[minimum_index][0]