
def is_sublist(test_list, sub_list):
    return any(sub_list == list(i) for i in zip(test_list,test_list[1:]))


