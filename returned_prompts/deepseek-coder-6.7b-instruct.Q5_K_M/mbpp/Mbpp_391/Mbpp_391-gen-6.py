
def convert_list_dictionary(lst1, lst2, lst3):
    return [{lst1[i]: {lst2[i]: lst3[i]}} for i in range(len(lst1))]


