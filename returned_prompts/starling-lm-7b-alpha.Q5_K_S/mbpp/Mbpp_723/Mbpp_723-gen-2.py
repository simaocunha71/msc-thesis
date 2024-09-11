def count_same_pair(list1, list2):
    same_pair_count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i]:
            same_pair_count += 1
    return same_pair_count

assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4

# def count_same_pair(list1, list2):
#     same_pair_count = 0
#     for i in zip(list1, list2):
#         if i[0] == i[1]:
#             same_pair_count += 1
#     return same_pair_count

# assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4

# def count_same_pair(list1, list2):
#     same_pair_count = 0
#     for i in range(len(list1)):
#         if list1[i] == list2[i]:
#             same_pair_count += 1
#     return same_pair_count

# assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6, 7, 9])==4


"""
def count_same_pair(list1, list2):
    same_pair_count = 0
    for i in zip(list1, list2):
        if i[0] == i[1]:
            same_pair_count += 1
    return same_pair_count

assert count_same_pair([1, 2, 3, 4, 5, 6, 7, 8],[2, 2, 3, 1, 2, 6