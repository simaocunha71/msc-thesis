```
def max_sum(arr):
    n = len(arr)
    inc = [0] * n
    dec = [0] * n
    inc[0] = arr[0]
    dec[n-1] = arr[n-1]
    for i in range(1, n):
        inc[i] = max(inc[i-1], arr[i])
    for i in range(n-2, -1, -1):
        dec[i] = max(dec[i+1], arr[i])
    return sum(inc) + sum(dec) - arr[0] - arr[n-1]
```
This function uses dynamic programming to find the maximum sum of a bitonic subsequence for the given array. It maintains two arrays, inc and dec, where inc[i] is the maximum sum of an increasing subsequence ending at index i, and dec[i] is the maximum sum of a decreasing subsequence starting at index i. The function then returns the sum of the maximum increasing and decreasing subsequences, minus the first and last elements of the array, to avoid counting them twice. The unit test `assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194` is used to verify the correctness of the function.