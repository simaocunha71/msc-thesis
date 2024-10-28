
def check_occurences(my_list):
    occurences = {}
    for tuple in my_list:
        if tuple in occurences:
            occurences[tuple] += 1
        else:
            occurences[tuple] = 1
    return occurences


