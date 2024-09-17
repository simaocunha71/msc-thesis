def extract_index_list(test_list1, test_list2, test_list3):
    common_elements = []
    for i in range(len(test_list1)):
        if test_list1[i] == test_list2[i] == test_list3[i]:
            common_elements.append(test_list1[i])
    return common_elements