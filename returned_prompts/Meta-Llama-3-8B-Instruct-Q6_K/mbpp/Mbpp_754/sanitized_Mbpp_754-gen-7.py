def extract_index_list(list1, list2, list3):
    common_list = [i for i in range(len(list1)) if list1[i] in list2 and list1[i] in list3]
    return [list1[i] for i in common_list]