def convert_list_dictionary(list1, list2, list3):
    d = {}
    for i in range(len(list1)):
        d[list1[i]] = {}
        d[list1[i]][list2[i]] = list3[i]
    return d
list1 = ["S001", "S002", "S003", "S004"]
list2 = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"]