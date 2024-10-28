def check_occurences(list_of_tuples):
    occurences = {}
    for i in list_of_tuples:
        if i not in occurences:
            occurences[i] = 1
        else:
            occurences[i] += 1
    return occurences