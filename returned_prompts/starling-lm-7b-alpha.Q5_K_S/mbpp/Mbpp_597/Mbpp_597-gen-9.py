"""
def find_kth(A, B, k):
    if len(A) < k:
        return B[k-1]
    elif len(B) < k:
        return A[k-1]
    else:
        if A[k-1] > B[k-1]:
            return find_kth(A[:k-1], B, k)
        else:
            return find_kth(A, B[:k-1], k)

assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
"""

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

assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6

"""

