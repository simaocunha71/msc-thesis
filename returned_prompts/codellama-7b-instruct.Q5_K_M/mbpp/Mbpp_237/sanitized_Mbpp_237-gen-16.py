def check_occurences(my_list_of_tuples):
    unique_tuples = {}
    for tuple in my_list_of_tuples:
        if tuple not in unique_tuples:
            unique_tuples[tuple] = 1
        else:
            unique_tuples[tuple] += 1
    return unique_tuples