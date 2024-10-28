    l_sorted = sorted(l[::2])
    l_even = l[::2]

    for index, value in enumerate(l_even):
        l_even[index] = l_sorted[index]

    return l_even


