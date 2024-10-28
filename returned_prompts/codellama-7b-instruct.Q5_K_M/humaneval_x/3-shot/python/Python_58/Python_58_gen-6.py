    common_elems = []

    for elem in l1:
        if elem in l2:
            common_elems.append(elem)

    return sorted(set(common_elems))


