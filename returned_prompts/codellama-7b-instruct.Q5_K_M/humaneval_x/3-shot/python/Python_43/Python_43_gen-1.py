    l = list(set(l))
    for i in l:
        for j in l:
            if i + j == 0 and i != j:
                return True

    return False


