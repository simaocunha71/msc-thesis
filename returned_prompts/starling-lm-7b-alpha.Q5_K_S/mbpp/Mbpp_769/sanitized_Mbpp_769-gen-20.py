def Diff(list_1: list, list_2: list) -> list:
    list_1 = set(list_1)
    list_2 = set(list_2)
    return [i for i in list_1 if i not in list_2]