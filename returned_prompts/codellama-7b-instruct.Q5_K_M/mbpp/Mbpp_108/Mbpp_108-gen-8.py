
def merge_sorted_list(list1, list2, list3):
    result = []
    list1 = iter(list1)
    list2 = iter(list2)
    list3 = iter(list3)
    while True:
        try:
            l1 = next(list1)
            l2 = next(list2)
            l3 = next(list3)
        except StopIteration:
            break
        if l1 <= l2 and l1 <= l3:
            result.append(l1)
        if l2 <= l1 and l2 <= l3:
            result.append(l2)
        if l3 <= l1 and l3 <= l2:
            result.append(l3)
    for i in list1:
        result.append(i)
    for i in list2:
        result.append(i)
    for i in list3:
        result.append(i)
    result.sort()
    return result


