def merge(lists):
    list1, list2 = [], []
    for sublist in lists:
        list1.append(sublist[0])
        list2.append(sublist[1])
    return [list1, list2]  # or return [list1 + list2] for a single list