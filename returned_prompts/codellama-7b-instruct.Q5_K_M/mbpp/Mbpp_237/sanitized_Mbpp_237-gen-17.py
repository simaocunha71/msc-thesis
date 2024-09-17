def check_occurences(my_list_of_tuples):
    occurences = {}
    for tuple_item in my_list_of_tuples:
        if tuple_item in occurences:
            occurences[tuple_item] += 1
        else:
            occurences[tuple_item] = 1
    return occurences