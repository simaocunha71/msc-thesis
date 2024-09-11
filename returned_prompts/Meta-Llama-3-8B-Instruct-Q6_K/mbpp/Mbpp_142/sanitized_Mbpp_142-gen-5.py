def count_samepair(list1, list2, list3):
    return sum(a == b for a, b in zip(list1, list2)) + sum(a == b for a, b in zip(list1, list3)) - sum(a == b for a, b in zip(list2, list3))