
def merge_sorted_list(list1: list, list2: list, list3: list) -> list:
    list1.extend(list2)
    list1.extend(list3)
    list1.sort()
    return list1


