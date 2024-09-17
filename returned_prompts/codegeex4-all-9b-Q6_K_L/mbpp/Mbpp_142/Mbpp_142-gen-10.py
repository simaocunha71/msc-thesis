def count_samepair(list1, list2, list3):
    return sum(i == j == k for i, j, k in zip(list1, list2, list3))

