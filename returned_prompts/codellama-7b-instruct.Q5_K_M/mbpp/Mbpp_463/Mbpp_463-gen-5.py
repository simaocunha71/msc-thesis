"""
def max_subarray_product(A):
    max_pos, max_neg = 1, 1
    for i in range(1, len(A)):
        max_pos = max(max_pos * A[i], A[i])
        max_neg = max(max_neg * A[i], -A[i])
    return max(max_pos, max_neg)
"""