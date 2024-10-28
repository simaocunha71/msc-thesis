def pancake_sort(A):
    for n in range(len(A)-1, 0, -1):
        max_val = A[0]
        max_pos = 0
        for i in range(1, n+1):
            if A[i] > max_val:
                max_val = A[i]
                max_pos = i
        A[:max_pos+1] = A[:max_pos][::-1] + A[max_pos+1:max_pos+1] + A[max_pos+1:max_pos+1+n-max_pos]
    return A