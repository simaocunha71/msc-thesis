def max_Abs_Diff(arr):
    diff = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            diff = max(diff,abs(arr[i]-arr[j]))
    return diff