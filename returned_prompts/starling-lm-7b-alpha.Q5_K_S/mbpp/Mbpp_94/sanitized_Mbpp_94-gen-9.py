def index_minimum(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])[0][0]