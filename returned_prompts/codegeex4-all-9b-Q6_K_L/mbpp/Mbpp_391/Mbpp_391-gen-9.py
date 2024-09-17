def convert_list_dictionary(list1: list, list2: list, list3: list) -> list:
    nested_dict = []
    for i in range(len(list1)):
        inner_dict = {list1[i]: {list2[i]: list3[i]}}
        nested_dict.append(inner_dict)
    return nested_dict

