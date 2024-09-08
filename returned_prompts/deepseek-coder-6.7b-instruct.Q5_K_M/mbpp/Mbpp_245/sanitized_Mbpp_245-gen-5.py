def max_sum(arr):
    n = len(arr)
 
    # table to store the maximum sum of a bitonic subsequence upto index i
    msis = [0]*n
    msis[0] = arr[0]
 
    # table to store the maximum sum of a decreasing subsequence upto index i
    msds = [0]*n
    msds[0] = arr[0]
 
    # maximum sum of bitonic subsequence
    max_sum = arr[0]
 
    # fill the tables in bottom up manner
    for i in range(1, n):
        msis[i] = arr[i]
        msds[i] = arr[i]
 
        # compute sum of all increasing subsequences of arr[0..i]
        for j in range(i):
            if (arr[i] > arr[j] and msis[i] < msis[j]+arr[i]):
                msis[i] = msis[j] + arr[i]
 
        # compute sum of all decreasing subsequences of arr[0..i]
        for j in range(i):
            if (arr[i] < arr[j] and msds[i] < msds[j] + arr[i]):
                msds[i] = msds[j] + arr[i]
 
        # update maximum sum
        if (msis[i] > max_sum):
            max_sum = msis[i]
 
        if (msds[i] > max_sum):
            max_sum = msds[i]
 
    # return the maximum sum
    return max_sum