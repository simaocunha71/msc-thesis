
def average_tuple(tuple_of_tuples):
    list_of_averages = []
    for tup in tuple_of_tuples:
        list_of_averages.append(sum(tup) / len(tup))
    return list_of_averages


