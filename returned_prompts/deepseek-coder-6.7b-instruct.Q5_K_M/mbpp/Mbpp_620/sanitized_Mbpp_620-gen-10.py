def largest_subset(arr):
    arr.sort()
    n = len(arr)
    subset = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i]%arr[j] == 0 and subset[i]<subset[j]+1:
                subset[i] = subset[j]+1
    maximum = 0
    for i in range(len(subset)):
        maximum = max(maximum, subset[i])
    return maximum