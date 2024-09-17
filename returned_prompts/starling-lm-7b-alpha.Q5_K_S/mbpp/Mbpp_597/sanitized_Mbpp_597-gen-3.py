def find_kth(A, B, k):
    l = 0
    r = len(A) + len(B)

    while l < r:
        m = (l + r) // 2
        if A[m // len(A)] < B[m % len(B)]:
            l = m + 1
        else:
            r = m
    return A[l // len(A)]