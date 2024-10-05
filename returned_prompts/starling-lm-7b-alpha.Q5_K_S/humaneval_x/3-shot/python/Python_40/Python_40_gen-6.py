    l.sort()
    n = len(l)

    for i in range(n):
        for j in range(i + 1, n):
            k = l[i] + l[j]
            index = bisect_left(l, -k)
            if index < j and l[index] == -k:
                return True

    return False


