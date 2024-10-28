
def average_tuple(tuple_of_tuples: tuple) -> list:
    list_of_tuples = list(tuple_of_tuples)
    list_of_averages = []
    for i in list_of_tuples:
        sum = 0
        for j in i:
            sum += j
        average = sum/len(i)
        list_of_averages.append(average)
    return list_of_averages


