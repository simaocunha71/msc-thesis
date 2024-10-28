```
def max_sum(arr):
    n = len(arr)
    inc = [0] * n
    dec = [0] * n
    inc[0] = arr[0]
    dec[n - 1] = arr[n - 1]
    for i in range(1, n):
        inc[i] = max(inc[i - 1], arr[i])
    for i in range(n - 2, -1, -1):
        dec[i] = max(dec[i + 1], arr[i])
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, inc[i] + dec[i])
    return max_sum
```
This function works by first initializing two arrays `inc` and `dec` to keep track of the maximum increasing and decreasing subsequences ending at each position. It then fills up these arrays by iterating through the input array. Finally, it iterates through the arrays again to find the maximum sum of a bitonic subsequence. The time complexity is O(n), where n is the length of the input array. The space complexity is also O(n). 





