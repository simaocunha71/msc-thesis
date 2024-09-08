Here is a Python solution:

```python
def max_sum(arr):
    n = len(arr)

    # Initialize variables
    inc = [0]*n
    dec = [0]*n

    # Compute increasing sum
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and inc[i] < inc[j]:
                inc[i] = inc[j]
        inc[i] += arr[i]

    # Compute decreasing sum
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if arr[i] > arr[j] and dec[i] < dec[j]:
                dec[i] = dec[j]
        dec[i] += arr[i]

    # Find maximum sum of bitonic subsequence
    max_sum = arr[0]
    for i in range(1, n):
        for j in range(i):
            if inc[j] + dec[i] > max_sum:
                max_sum = inc[j] + dec[i]
        if arr[i] > max_sum:
            max_sum = arr[i]

    return max_sum
```
This function works by computing the maximum sum of an increasing subsequence ending at each index and the maximum sum of a decreasing subsequence starting at each index, then finding the maximum sum of a bitonic subsequence by adding the two sums at each index. The time complexity is O(n^2) due to the nested loops, and the space complexity is O(n) for the two auxiliary arrays.

Please note that the function assumes that the input array is a non-empty bitonic sequence, and that the decreasing part of the sequence must have at least one element. If these conditions are not met, the function may not behave as expected.

Also, the function returns the maximum sum of a bitonic subsequence, but it doesn't return the subsequence itself. If you need the subsequence as well, you would need to modify the function to keep track of the subsequence as well.

Please let me know if you have any questions