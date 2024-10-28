def find_kth(A, B, k):
    l = len(A)
    m = len(B)
    if l > m:
        return find_kth(B, A, k)
    if k == 0:
        return None