    l_even = [i for i, x in enumerate(l) if i % 2 == 0]
    l_even.sort()
    result = [l[i] for i in l_even]
    return result


