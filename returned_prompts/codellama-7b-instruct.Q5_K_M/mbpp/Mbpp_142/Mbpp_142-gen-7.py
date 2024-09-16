def count_samepair(list1, list2, list3):
    return sum(x == y for x, y in zip(list1, list2)) + sum(x == y for x, y in zip(list1, list3)) + sum(x == y for x, y in zip(list2, list3))
