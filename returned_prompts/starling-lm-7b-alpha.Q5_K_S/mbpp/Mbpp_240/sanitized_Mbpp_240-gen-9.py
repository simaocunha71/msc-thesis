def replace_list(list1, list2):
    # concatenate the two lists together
    new_list = list1 + list2
    # remove the last element of the new list
    new_list = new_list[:-len(list2)]
    # return the new list
    return new_list