    lst = [elem for elem in lst if len(elem) % 2 != 1]
    lst.sort(key=lambda elem: (len(elem), elem))
    return lst


