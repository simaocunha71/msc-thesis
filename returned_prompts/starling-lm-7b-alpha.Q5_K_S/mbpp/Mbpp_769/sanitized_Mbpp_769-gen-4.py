def Diff(list_one, list_two):
    result = [i for i in list_one if i not in list_two]
    return result