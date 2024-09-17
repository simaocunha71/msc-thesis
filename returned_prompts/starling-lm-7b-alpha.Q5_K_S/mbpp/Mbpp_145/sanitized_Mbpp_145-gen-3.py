def max_Abs_Diff(A):
    max_diff = 0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            diff = abs(A[i] - A[j])
            max_diff = max(max_diff, diff)
    return max_diff