
    # convert all items to set
    s1 = set(l1)
    s2 = set(l2)

    # find common elements
    common = s1.intersection(s2)

    # sort and return
    return sorted(common)