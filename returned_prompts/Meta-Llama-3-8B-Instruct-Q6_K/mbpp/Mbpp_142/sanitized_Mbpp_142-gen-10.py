def count_samepair(list1, list2, list3):
    return sum(i == j for i, j in zip(list1, list2, list3))  # using zip() to iterate over three lists simultaneously and count the number of identical items