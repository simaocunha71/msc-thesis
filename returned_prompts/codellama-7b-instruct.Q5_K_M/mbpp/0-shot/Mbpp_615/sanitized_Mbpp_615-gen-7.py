def average_tuple(tuple_of_tuple):
    list_of_average = []
    for tuple in tuple_of_tuple:
        sum_of_tuple = sum(tuple)
        average = sum_of_tuple / len(tuple)
        list_of_average.append(average)
    return list_of_average