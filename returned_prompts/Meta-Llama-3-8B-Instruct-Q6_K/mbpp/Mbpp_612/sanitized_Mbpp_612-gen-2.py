def merge(list_of_lists):
    return [list(map(lambda x: x[0], list_of_lists)), list(map(lambda x: x[1], list_of_lists))]