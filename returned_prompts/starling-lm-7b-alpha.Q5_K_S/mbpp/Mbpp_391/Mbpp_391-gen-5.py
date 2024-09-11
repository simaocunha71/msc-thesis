from collections import defaultdict


def convert_list_dictionary(list1, list2, list3):
    d = defaultdict(dict)
    for i in range(len(list1)):
        d[list1[i]] = {list2[i]: list3[i]}
    return list(d.values())


# assert convert_list_dictionary(["S001", "S002", "S003", "S004"], ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"], [85, 98, 89, 92]) == [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]


# print(convert_list_dictionary(["S001", "S002", "S003", "S004"], ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"], [85, 98, 89, 92]))




```

```
def convert_list_dictionary(list1, list2, list3):
    d = defaultdict(dict)
    for i in range(len(list1)):
        d[list1[i]] = {list2[i]: list3[i]}
    return list(d.values())


# assert convert_list_dictionary(["S001", "S002", "S003", "S004"], ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"], [85, 98, 89, 92]) == [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004