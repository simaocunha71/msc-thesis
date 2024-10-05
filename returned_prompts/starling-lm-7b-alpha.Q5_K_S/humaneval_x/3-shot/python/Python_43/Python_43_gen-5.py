    l.sort()
    return any(l[i] + l[len(l) - i - 1] == 0 for i in range(len(l) // 2))


