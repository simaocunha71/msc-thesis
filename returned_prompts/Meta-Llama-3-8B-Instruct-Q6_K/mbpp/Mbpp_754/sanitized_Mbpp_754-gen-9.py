def extract_index_list(list1, list2, list3):
    common_elements = set()
    for i in range(len(list1)):
        if list1[i] == list2[i] == list3[i] and list1[i] not in common_elements:
            common_elements.add(list1[i])
    return list(common_elements) if common_elements else []  # return empty list if no common elements found