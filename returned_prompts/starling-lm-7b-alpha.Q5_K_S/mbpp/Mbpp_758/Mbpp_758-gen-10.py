def unique_sublists(input_list):
    my_dict = {}
    for sublist in input_list:
        if sublist not in my_dict:
            my_dict[sublist] = 1
        else:
            my_dict[sublist] += 1
    return my_dict


def unique_sublists(input_list):
    my_dict = {}
    for sublist in input_list:
        if sublist not in my_dict:
            my_dict[tuple(sublist)] = 1
        else:
            my_dict[tuple(sublist)] += 1
    return my_dict


def unique_sublists(input_list):
    my_dict = {}
    for sublist in input_list:
        my_dict[sublist] = my_dict.get(sublist, 0) + 1
    return my_dict

def unique_sublists(input_list):
    my_dict = {}
    for sublist in input_list:
        my_dict[tuple(sublist)] = my_dict.get(tuple(sublist), 0) + 1
    return my_dict

def unique_sublists(input_list):
    my_dict = {}
    for sublist in input_list:
        if type(sublist) is tuple:
            my_dict[sublist] = my_dict.get(sublist, 0) + 1
        else:
            my_dict[tuple(sublist)] = my_dict.get(tuple(sublist), 0) + 1
    return my_dict

def unique_sublists(input_list):
    my_dict = {}
    for sublist in input_list:
        my_dict[sublist] = my_dict.get(sublist, 0) + 1
    return my_dict

def unique_sublists(input_list):
    my_dict = {}
    for sublist in input_list:
        if type(sublist) is tuple:
            my_dict[sublist] = my_dict.get(sublist, 0) + 1
        else:
            my