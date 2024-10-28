def div_list(list1,list2):
    assert len(list1)==len(list2), "Lengths of the two lists must be same"
    res=[]
    for i in range(len(list1)):
        res.append(list1[i]/list2[i])
    return res