    lst = [x for x in lst if len(x) % 2 == 0]
    return sorted(lst, key=lambda x: (len(x), x))
