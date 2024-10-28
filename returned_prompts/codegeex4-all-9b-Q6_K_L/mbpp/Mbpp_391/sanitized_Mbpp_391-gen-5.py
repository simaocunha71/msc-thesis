def convert_list_dictionary(list1, list2, list3):
    result = []
    for i in range(len(list1)):
        dic = {list1[i]: {list2[i]: list3[i]}}
        result.append(dic)
    return result