    l1.sort()
    l2.sort()
    result = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            i += 1
        elif l1[i] == l2[j]:
            result.append(l1[i])
            i += 1
            j += 1
        else:
            j += 1
    return result


