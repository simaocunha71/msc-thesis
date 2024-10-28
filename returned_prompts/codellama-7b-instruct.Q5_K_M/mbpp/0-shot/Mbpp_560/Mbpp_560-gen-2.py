def union_elements(tuple1, tuple2):
    list1 = list(tuple1)
    list2 = list(tuple2)
    list3 = list1 + list2
    set3 = set(list3)
    list4 = list(set3)
    list4.sort()
    return tuple(list4)


