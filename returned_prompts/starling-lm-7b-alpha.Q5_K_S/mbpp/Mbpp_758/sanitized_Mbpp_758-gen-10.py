def unique_sublists(input_list):
    my_dict = {}
    for sublist in input_list:
        if sublist not in my_dict:
            my_dict[sublist] = 1
        else:
            my_dict[sublist] += 1
    return my_dict