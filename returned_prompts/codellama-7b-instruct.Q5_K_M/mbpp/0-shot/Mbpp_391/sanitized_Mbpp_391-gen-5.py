def convert_list_dictionary(list_1,list_2,list_3):
    return [ {list_1[i]: {list_2[i]: list_3[i]}} for i in range(len(list_1)) ]