def find_kth(A, B, k):
    a, b = len(A), len(B)
    while a != b:
        if a < b:
            a += 1
            A += B[a]
        else:
            b += 1
            B += A[b]
    return A[k] if k < b else B[k]