def swap_List(list):
    size = len(list)
    list[0], list[size - 1] = list[size - 1], list[0]
    return list