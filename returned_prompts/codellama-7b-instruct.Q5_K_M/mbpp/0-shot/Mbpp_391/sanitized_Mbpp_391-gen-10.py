def convert_list_dictionary(list_1,list_2,list_3):
    list_dict = dict(zip(list_1, list_2))
    dict_list = [dict(zip(list_1, [list_3])) for list_3 in list_3]
    return [dict(zip(list_1, [dict_list[list_1]])) for list_1 in list_1]