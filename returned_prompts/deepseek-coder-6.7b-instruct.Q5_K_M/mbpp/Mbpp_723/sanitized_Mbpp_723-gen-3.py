def count_same_pair(list1, list2):
    return sum(1 for a, b in zip(list1, list2) if a == b)