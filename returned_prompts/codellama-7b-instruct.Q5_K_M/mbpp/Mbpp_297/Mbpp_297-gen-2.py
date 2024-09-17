
def flatten_list(my_list):
    flat_list = []
    for element in my_list:
        if type(element) == list:
            flat_list += flatten_list(element)
        else:
            flat_list.append(element)
    return flat_list


