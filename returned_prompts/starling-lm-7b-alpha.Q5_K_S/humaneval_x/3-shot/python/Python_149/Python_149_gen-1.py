    # First, remove all strings with odd length
    lst = [x for x in lst if len(x) % 2 == 0]
    lst.sort(key=len)
    return lst


