def Diff(li1, li2): 
    return list(set(li1) - set(li2))
print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))