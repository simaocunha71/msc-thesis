def get_median(list1, list2, n):
    i = 0
    j = 0
    m1 = -1
    m2 = -1

    for _ in range(n):
        if i == n:
            m1 = m2
            m2 = list2[0]
            break
        if j == n:
            m1 = m2
            m2 = list1[0]
            break

        if list1[i] <= list2[j]:
            m1 = m2
            m2 = list1[i]
            i += 1
        else:
            m1 = m2
            m2 = list2[j]
            j += 1

    return (m1 + m2) / 2