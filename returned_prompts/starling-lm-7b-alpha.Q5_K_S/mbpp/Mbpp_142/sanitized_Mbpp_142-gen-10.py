def count_samepair(lst1,lst2,lst3):
    samepair = 0
    for i in range(len(lst1)):
        if lst1[i] == lst2[i] == lst3[i]:
            samepair += 1
    return samepair