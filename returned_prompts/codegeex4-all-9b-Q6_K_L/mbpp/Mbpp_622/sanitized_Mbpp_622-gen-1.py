def get_median(A, B, n):
    # Merge the two lists into one sorted list
    merged = []
    i, j = 0, 0
    while i < n and j < n:
        if A[i] < B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1
    # Add the remaining elements from A or B
    while i < n:
        merged.append(A[i])
        i += 1
    while j < n:
        merged.append(B[j])
        j += 1

    # Find the median
    if n % 2 == 0:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2
    else:
        return merged[n // 2]