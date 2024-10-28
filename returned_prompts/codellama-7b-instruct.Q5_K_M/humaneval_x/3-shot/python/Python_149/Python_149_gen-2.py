    lst = [word for word in lst if len(word) % 2 == 0]
    lst.sort(key=len)
    lst.sort()
    return lst


