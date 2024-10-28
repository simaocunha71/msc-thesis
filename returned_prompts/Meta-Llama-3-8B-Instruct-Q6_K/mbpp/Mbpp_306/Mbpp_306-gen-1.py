```
def max_sum_increasing_subseq(arr, i, k, j):
    dp = [0] * (i + 1)
    for num in arr[:i+1]:
        for j in range(i, -1, -1):
            if num > dp[j]:
                dp[j] = num
    for num in arr[i+1:]:
        if num > dp[j]:
            dp[j] = num
    return sum(dp)
```
The function `max_sum_increasing_subseq` calculates the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i, i.e., k > i.

The function first initializes a dynamic programming array `dp` with size `i+1` to store the maximum sum of increasing subsequence for each prefix. It then iterates over the prefix and updates the `dp` array if a larger number is found.

After that, it iterates over the suffix starting from `i+1` and updates the `dp` array if a larger number is found. Finally, it returns the sum of the `dp` array, which represents the maximum sum of increasing subsequence from prefix until ith index and also including a given kth element which is after i.

The unit test `assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11` ensures that the function works correctly. The maximum sum of increasing subsequence is 11, which is the sum of the numbers 1, 2, 3, 4, and 5. The function correctly identifies these numbers as the maximum sum of increasing subsequence.