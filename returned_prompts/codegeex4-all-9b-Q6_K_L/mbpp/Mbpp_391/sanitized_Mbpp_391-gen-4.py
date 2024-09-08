def convert_list_dictionary(list1, list2, list3):
    res = []
    for i in range(len(list1)):
        res.append({list1[i]: {list2[i]: list3[i]}})
    return res