def max_Abs_Diff(arr):
    # Write your code here
    return max(abs(arr[i]-arr[j]) for i in range(len(arr)) for j in range(i+1, len(arr)))