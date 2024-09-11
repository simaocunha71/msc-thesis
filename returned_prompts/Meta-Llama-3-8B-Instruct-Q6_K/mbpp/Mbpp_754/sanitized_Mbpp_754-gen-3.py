def extract_index_list(list1, list2, list3):
    common_elements = [i for i in set(list1) if list1.count(i) > 0 and list2.count(i) > 0 and list3.count(i) > 0]
    return common_elements