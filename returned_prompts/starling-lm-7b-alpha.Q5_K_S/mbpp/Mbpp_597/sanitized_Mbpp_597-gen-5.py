def find_kth(A, B, k):
    if k > len(A) + len(B):
        return None
    elif k == 0:
        return A[0]
    elif k == len(A) + len(B):
        return B[0]
    else:
        if A[len(A) - k] < B[len(B) - k]:
            return find_kth(A, B, k - len(A))
        else:
            return find_kth(A, B, k - len(B))