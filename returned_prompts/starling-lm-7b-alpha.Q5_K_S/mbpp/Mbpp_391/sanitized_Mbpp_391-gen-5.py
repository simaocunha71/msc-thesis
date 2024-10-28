from collections import defaultdict
def convert_list_dictionary(list1, list2, list3):
    d = defaultdict(dict)
    for i in range(len(list1)):
        d[list1[i]] = {list2[i]: list3[i]}
    return list(d.values())