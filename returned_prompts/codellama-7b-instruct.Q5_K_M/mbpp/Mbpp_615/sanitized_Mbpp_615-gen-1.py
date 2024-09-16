def average_tuple(tuple_of_tuples):
    average_list = []
    for t in tuple_of_tuples:
        average_list.append(sum(t) / len(t))
    return average_list