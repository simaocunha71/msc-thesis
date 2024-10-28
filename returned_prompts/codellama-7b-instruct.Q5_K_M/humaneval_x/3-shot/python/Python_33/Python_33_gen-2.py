    l_sorted = sorted(l)
    l_sorted_third = []

    for idx, elem in enumerate(l):
        if idx % 3 == 0:
            l_sorted_third.append(elem)
        else:
            l_sorted_third.append(l_sorted[idx])

    return l_sorted_third


