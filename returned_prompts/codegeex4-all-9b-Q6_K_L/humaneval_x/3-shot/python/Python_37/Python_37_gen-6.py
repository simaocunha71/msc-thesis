    l_even = sorted([l[i] for i in range(0, len(l), 2)])
    l_sorted = []
    for i in range(len(l)):
        if i % 2 == 0:
            l_sorted.append(l_even.pop(0))
        else:
            l_sorted.append(l[i])

    return l_sorted

