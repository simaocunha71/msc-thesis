def convert_list_dictionary(list1, list2, list3):
    return [dict(zip(list1, zip(list2, list3))) for i in range(len(list1))]


