Here's one possible solution:

```python
def max_sum_increasing_subseq(arr, i, k, n):
    if k > n:
        return -float('inf')
    if k == n:
        return arr[k-1]
    max_sum_until_i = [0]*i
    max_sum_until_i[0] = arr[0]
    for j in range(1, i):
        max_sum_until_i[j] = max(max_sum_until_i[j-1], arr[j])
    max_sum_from_k = arr[k-1]
    for j in range(k-2, -1, -1):
        if arr[j] < arr[j+1]:
            max_sum_from_k += arr[j]
        else:
            max_sum_from_k = arr[j]
    return max(max_sum_until_i[i-1], max_sum_from_k)
```

This function first initializes a list `max_sum_until_i` with length `i` to store the maximum sum of increasing subsequence until `i` index. Then it iterates from index 1 to `i` and updates `max_sum_until_i` by comparing the maximum sum of increasing subsequence until previous index with the current element of `arr`. After that, it initializes a variable `max_sum_from_k` with the value of `arr[k-1]` to store the maximum sum of increasing subsequence starting from `k` index. Then it iterates from `k-2` to `0` (inclusive) and checks if the current element of `arr` is smaller than the next element. If so, it adds the current element to `max_sum_from_k`, otherwise it updates `max_sum_from_k` with the current element. Finally, it returns the maximum value between `max_sum_until_i[i-1]` and `max_sum_from_k`.

Note: The function assumes that `arr` is a list of positive integers and `i` and `n` are positive integers less than the length of `arr`.

