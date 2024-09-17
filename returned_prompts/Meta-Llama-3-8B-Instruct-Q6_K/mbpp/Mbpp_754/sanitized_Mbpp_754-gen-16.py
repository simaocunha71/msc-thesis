import itertools
def extract_index_list(list1, list2, list3):
    if len(list1) != len(list2) or len(list1) != len(list3):
        return "Lists must be of the same length"
    common_index_list = [i for i in range(len(list1)) if list1[i] in list2 and list1[i] in list3]
    return [list1[i] for i in common_index_list]