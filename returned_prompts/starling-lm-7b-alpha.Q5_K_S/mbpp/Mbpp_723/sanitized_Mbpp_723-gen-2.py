def count_same_pair(list1, list2):
    same_pair_count = 0
    for i in zip(list1, list2):
        if i[0] == i[1]:
            same_pair_count += 1
    return same_pair_count