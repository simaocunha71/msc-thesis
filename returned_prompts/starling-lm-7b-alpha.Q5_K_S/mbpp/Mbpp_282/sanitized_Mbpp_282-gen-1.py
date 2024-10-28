def sub_list(l1,l2):
    assert len(l1)==len(l2)
    l3=[l1[i]-l2[i] for i in range(len(l1))]
    return l3