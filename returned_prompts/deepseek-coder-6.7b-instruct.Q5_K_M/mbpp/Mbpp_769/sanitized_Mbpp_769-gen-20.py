def Diff(li1, li2): 
    return list(filter(lambda x: x not in li2, li1))