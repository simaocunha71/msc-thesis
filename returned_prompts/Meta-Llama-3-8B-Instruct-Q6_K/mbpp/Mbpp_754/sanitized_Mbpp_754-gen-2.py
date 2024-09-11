def extract_index_list(list1, list2, list3):
    common = [i for i in range(len(list1)) if list1[i] == list2[i] == list3[i]]
    return [i for i in common if list1[i] in [list2[i], list3[i]]] if common else []