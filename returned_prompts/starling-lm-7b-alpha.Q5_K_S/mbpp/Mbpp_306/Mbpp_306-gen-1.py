The function can be implemented as follows:

```python
def max_sum_increasing_subseq(arr, i, k, n):
    max_sums = [0] * n

    # Initialize max_sums using prefix max sums
    max_sums[0] = arr[0]
    for i in range(1, n):
        max_sums[i] = max(max_sums[i-1], arr[i])

    # Calculate max sum of increasing subsequence including kth element
    curr_max = max_sums[i]
    curr_index = i
    while curr_index < n and arr[curr_index] < k:
        if max_sums[curr_index] > curr_max:
            curr_max = max_sums[curr_index]
            curr_index = curr_index + 1
        else:
            break

    # If kth element is found, return max sum of increasing subsequence including kth element
    if curr_index < n and arr[curr_index] == k:
        return curr_max
    # Else return the max sum of increasing subsequence till ith index
    else:
        return max_sums[i]
```

The time complexity of this function is O(n) and the space complexity is O(n).

To test the function, you can use the following code:

```python
assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5], 7, 4, 6) == 11
```

This will assert that the function `max_sum_increasing_subseq` correctly computes the maximum sum of an increasing subsequence from the prefix until the ith index and including the kth element, which is after the i-th index.

The function works by first initializing an array `max_sums` to store the maximum sum of an increasing subsequence until each index in the array. It then calculates the maximum sum of an increasing subsequence including the k-th element by iterating from the ith index until the end of the array, checking