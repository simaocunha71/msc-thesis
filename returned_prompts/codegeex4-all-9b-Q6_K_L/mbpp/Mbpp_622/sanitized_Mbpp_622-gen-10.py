def get_median(l1, l2, n):
    """Find the median of two sorted lists of same size."""
    i, j = 0, 0
    m1, m2 = 0, 0
    while i + j <= n:
        if i == n:
            m2 = l2[j]
            j += 1
        elif j == n:
            m1 = l1[i]
            i += 1
        elif l1[i] < l2[j]:
            m1 = l1[i]
            i += 1
        else:
            m2 = l2[j]
            j += 1
    return (m1 + m2) / 2.0