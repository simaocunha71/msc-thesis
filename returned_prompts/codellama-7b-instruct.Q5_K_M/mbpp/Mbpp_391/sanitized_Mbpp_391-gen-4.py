def convert_list_dictionary(list1,list2,list3):
    if len(list1) == len(list2) == len(list3):
        return [ {list1[i]:{list2[i]:list3[i]}} for i in range(len(list1)) ]
    else:
        return None