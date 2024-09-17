
def average_tuple(tuple_of_tuples):
    list_of_averages = []
    for inner_tuple in tuple_of_tuples:
        average = sum(inner_tuple) / len(inner_tuple)
        list_of_averages.append(average)
    return list_of_averages


