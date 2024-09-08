This problem can be solved using a dynamic programming approach. The idea is to create two arrays, one to store the maximum sum at each index, and another to store the maximum sum ending at the index after k. 

The function would look something like this:

```python
def max_sum_increasing_subseq(arr, n, k, i):
    # Initialize the dp arrays
    dp = [0] * n
    post_k_dp = [0] * n
    
    # Base case
    dp[0] = arr[0]
    
    # Fill the dp array
    for j in range(1, n):
        dp[j] = arr[j]
        for i in range(j):
            if arr[i] < arr[j]:
                dp[j] = max(dp[j], dp[i] + arr[j])
    
    # Fill the post_k_dp array
    post_k_dp[k] = arr[k]
    for j in range(k+1, n):
        post_k_dp[j] = max(post_k_dp[j-1], dp[j-1] + arr[j])

    # Return the maximum sum
    return max(dp[i], post_k_dp[i])
```

This function first initializes the dp and post_k_dp arrays with the base case (dp[0] = arr[0]). Then it fills the dp array by iterating through the array and updating the maximum sum at each index. After that, it fills the post_k_dp array by iterating from k to the end of the array and updating the maximum sum ending at each index. Finally, it returns the maximum sum at the given index i.

Please note that this function assumes that the input array is 0-indexed. Also, the function doesn't handle the case where k is out of the range of the array. You may need to add error checking code to handle such cases.
"""

