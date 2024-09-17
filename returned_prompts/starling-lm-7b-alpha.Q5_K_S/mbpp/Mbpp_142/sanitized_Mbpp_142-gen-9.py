def count_samepair(list1,list2,list3):
    same_pair_count = 0
    for i in range(0,len(list1)):
        if list1[i] == list2[i] == list3[i]:
            same_pair_count += 1
    return same_pair_count