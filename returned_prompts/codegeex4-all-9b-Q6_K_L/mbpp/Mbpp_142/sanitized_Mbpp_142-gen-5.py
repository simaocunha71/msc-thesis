def count_samepair(l1,l2,l3):
    c = 0
    for i in range(len(l1)):
        if l1[i] == l2[i] == l3[i]:
            c += 1
    return c