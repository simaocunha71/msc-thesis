def div_list(l1, l2):
    assert len(l1) == len(l2), "The length of both the list should be equal"
    res = []
    for i in range(len(l1)):
        res.append(l1[i]/l2[i])
    return res