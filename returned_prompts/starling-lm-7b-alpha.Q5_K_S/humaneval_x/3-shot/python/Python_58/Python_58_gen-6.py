    l1.sort()
    l2.sort()
    index1 = 0
    index2 = 0
    result = []
    while index1 < len(l1) and index2 < len(l2):
        if l1[index1] == l2[index2]:
            result.append(l1[index1])
            index1 += 1
            index2 += 1
        elif l1[index1] < l2[index2]:
            index1 += 1
        else:
            index2 += 1
    return result


