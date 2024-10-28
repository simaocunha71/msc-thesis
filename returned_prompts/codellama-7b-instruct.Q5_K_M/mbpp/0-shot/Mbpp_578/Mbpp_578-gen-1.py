
def interleave_lists(list_of_lists):
    flat_list = []
    for i in range(len(list_of_lists[0])):
        for lists in list_of_lists:
            flat_list.append(lists[i])
    return flat_list
