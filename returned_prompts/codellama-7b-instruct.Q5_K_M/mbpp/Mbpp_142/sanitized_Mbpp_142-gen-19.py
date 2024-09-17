def count_samepair(list1, list2, list3):
    return sum(i == j and k == l for i, j, k, l in zip(list1, list2, list3))