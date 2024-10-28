def find_kth(A, B, k):
    if len(A) > len(B):
        return find_kth(B, A, k)
    if k == 0:
        return None
    if k > len(A):
        return A[-1]

    left = 0
    right = len(A)

    while left < right:
        mid = left + (right - left) // 2
        if A[mid] > B[k - 1]:
            right = mid
        else:
            left = mid + 1
    return A[left]