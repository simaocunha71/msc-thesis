    result = []
    l1.sort()
    l2.sort()
    idx1, idx2 = 0, 0

    while idx1 < len(l1) and idx2 < len(l2):
        if l1[idx1] == l2[idx2]:
            result.append(l1[idx1])
            idx1 += 1
            idx2 += 1
        elif l1[idx1] < l2[idx2]:
            idx1 += 1
        else:
            idx2 += 1

    return result


