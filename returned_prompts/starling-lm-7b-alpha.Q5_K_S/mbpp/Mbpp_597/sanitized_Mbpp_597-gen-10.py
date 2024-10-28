def find_kth(A, B, k):
    m = len(A)
    n = len(B)
    if m + n < k or k <= 0:
        return None
    if m == 0:
        return B[k-1]
    if n == 0:
        return A[k-1]
    if A[m-1] > B[n-1]:
        return find_kth(A, B, k, m, n)
    else:
        return find_kth(B, A, k, n, m)