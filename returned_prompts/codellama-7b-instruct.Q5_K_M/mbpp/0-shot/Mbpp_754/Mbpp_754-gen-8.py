def extract_index_list(list1, list2, list3):
    common_elements = []
    for i in range(len(list1)):
        if list1[i] == list2[i] == list3[i]:
            common_elements.append(list1[i])
    return common_elements
