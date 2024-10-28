    s = set()
    for x in l:
        if x * -1 in s:
            return True
        s.add(x)
    return False


