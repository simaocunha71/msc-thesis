def index_minimum(list_of_tuples):
    min_tuple = min(list_of_tuples, key = lambda x: x[1])
    return min_tuple[0]
list_of_tuples = [('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]