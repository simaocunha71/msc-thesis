
def convert_list_dictionary(list1, list2, list3):
    return [dict(zip(list1, [dict(zip(list2, value)) for value in zip(*[list2, list3])])) for list2, list3 in zip(list2, list3)]



