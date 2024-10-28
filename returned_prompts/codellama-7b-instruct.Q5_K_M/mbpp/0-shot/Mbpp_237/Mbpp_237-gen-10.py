def check_occurences(my_list):
    my_dict = {}
    for item in my_list:
        if item not in my_dict:
            my_dict[item] = 1
        else:
            my_dict[item] += 1
    return my_dict


