
def check_occurences(list_of_tuples):
    dict_of_occurences = {}
    for i in range(len(list_of_tuples)):
        if list_of_tuples[i] in dict_of_occurences:
            dict_of_occurences[list_of_tuples[i]] += 1
        else:
            dict_of_occurences[list_of_tuples[i]] = 1
    return dict_of_occurences



