def average_tuple(tuple_of_tuples):
    list_of_averages = []
    for each_tuple in tuple_of_tuples:
        average = sum(each_tuple) / len(each_tuple)
        list_of_averages.append(average)
    return list_of_averages



