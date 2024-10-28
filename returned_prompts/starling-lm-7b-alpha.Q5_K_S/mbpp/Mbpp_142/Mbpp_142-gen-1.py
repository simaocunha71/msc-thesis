
def count_samepair(list1, list2, list3):
    return sum(1 for i, j, k in zip(list1, list2, list3) if i==j==k)


