def all_unique(lst):
    s = set()
    for i in lst:
        if i in s:
            return False
        s.add(i)
    return True