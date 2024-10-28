    l.sort()
    n = len(l)
    for i in range(n):
        j = n - 1 - i
        if l[i] + l[j] == 0:
            return True
        if i != j and l[i] + l[j] > 0:
            return False
    return False


