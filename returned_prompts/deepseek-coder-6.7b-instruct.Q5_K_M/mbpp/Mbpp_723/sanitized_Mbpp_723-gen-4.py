def count_same_pair(l1, l2):
    count = 0
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            count += 1
    return count