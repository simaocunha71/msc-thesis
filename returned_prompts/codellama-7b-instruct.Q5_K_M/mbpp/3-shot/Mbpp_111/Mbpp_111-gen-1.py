
def common_in_nested_lists(my_list):
    common_elements = []
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            common_elements += list(set(my_list[i]) & set(my_list[j]))
    return common_elements


