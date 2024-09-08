def Diff(lst1, lst2):
    return [i for i in lst1 if i not in lst2]
lst1 = [10, 15, 20, 25, 30, 35, 40]
lst2 = [25, 40, 35]