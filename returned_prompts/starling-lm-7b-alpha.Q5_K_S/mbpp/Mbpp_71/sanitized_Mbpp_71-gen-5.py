def comb_sort(A):
    n = len(A)
    gap = n
    swapped = True
    while gap != 1 or swapped:
        gap = max(1, int(gap/1.3))
        swapped = False
        for i in range(n - gap):
            if A[i] > A[i + gap]:
                A[i], A[i + gap] = A[i + gap], A[i]
                swapped = True
    return A