
def check_occurences(my_list):
    unique_tuples = []
    my_dict = {}

    for tups in my_list:
        if tups not in unique_tuples:
            unique_tuples.append(tups)

    for tups in unique_tuples:
        count = 0
        for item in my_list:
            if tups == item:
                count += 1
        my_dict[tups] = count
    return my_dict


