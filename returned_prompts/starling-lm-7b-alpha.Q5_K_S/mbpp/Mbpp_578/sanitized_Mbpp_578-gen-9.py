def interleave_lists(list1,list2,list3):
    list4 = []
    for i in range(len(list1)):
        list4.extend([list1[i],list2[i],list3[i]])
    return list4