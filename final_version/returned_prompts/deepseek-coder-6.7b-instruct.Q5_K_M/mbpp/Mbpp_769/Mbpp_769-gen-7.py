def Diff(lst1, lst2):
    return [i for i in lst1 if i not in lst2]

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))  # == [10, 20, 30, 15]

