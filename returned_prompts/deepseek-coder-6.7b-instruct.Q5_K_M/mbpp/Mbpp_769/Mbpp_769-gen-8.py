def Diff(list1, list2):
    return [i for i in list1 if i not in list2]

print(Diff([10, 15, 20, 25, 30, 35, 40], [25, 40, 35]))  # == [10, 20, 30, 15]


