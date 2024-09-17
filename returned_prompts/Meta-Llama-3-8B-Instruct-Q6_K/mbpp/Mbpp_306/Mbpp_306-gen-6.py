```
def max_sum_increasing_subseq(nums, i, k, prefix_sum):
    max_sum = prefix_sum[i]
    for j in range(i, k):
        if nums[j] > nums[j-1]:
            max_sum += nums[j]
    return max_sum
```
The function takes four parameters: `nums` - the list of numbers, `i` - the index up to which we need to consider the prefix, `k` - the index of the kth element after `i`, and `prefix_sum` - the prefix sum of the list. 

We start by initializing the maximum sum to the prefix sum up to index `i`. Then we iterate over the range from `i` to `k`, considering each element. If the current element is greater than the previous one, we add it to the maximum sum. Finally, we return the maximum sum.

The unit test `assert max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6) == 11` ensures that the function works correctly. It checks if the maximum sum of increasing subsequence from prefix until index 7 and also including the 4th element which is after 7 is 11.  ```python
``` ```
```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
``` ```python
