def count_same_pair(list1, list2):
    return sum(i == j for i, j in zip(list1, list2))

