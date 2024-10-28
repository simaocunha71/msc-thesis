def find_kth(A, B, k):
    if len(A) > len(B):
        A, B = B, A
    if k == 0:
        return B[0]
    if k > len(A) + len(B):
        return None
    left, right = 0, len(A)
    while left < right:
        mid = (left + right) // 2
        if A[mid] == B[mid]:
            if k == mid + 1:
                return A[mid]
            left = mid + 1
        elif A[mid] < B[mid]:
            if k <= mid + len(B):
                right = mid
            else:
                left = mid + 1
        else:
            if k <= mid + len(A):
                left = mid + 1
            else:
                right = mid
    return A[left]