The function can be implemented using Kadane's algorithm. This algorithm is used to find the largest sum of a contiguous array. The algorithm works by iterating through the array and updating the max sum and current sum at each step. The current sum is reset to 0 if it becomes negative. The max sum is updated if the current sum is greater than the max sum.

Here is the Python code for the problem:

```python
def max_sub_array_sum_repeated(arr, k, t):
    # Calculate the maximum subarray sum for the original array
    max_sum = curr_sum = max(arr)
    for i in range(t):
        for num in arr:
            curr_sum = max(curr_sum + num, num)
            max_sum = max(max_sum, curr_namedtuple.curr_sum)
        arr = arr[1:] + arr[:1]
    return max_sum * k

print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3))
```

This code first calculates the maximum subarray sum for the original array. Then it rotates the array by one element to the left and repeats the process k times. Finally, it returns the maximum sum multiplied by k.

Please note that this solution assumes that the array contains at least one positive number. If there are negative numbers in the array, the maximum sum might be zero, which is not what we want in this case.

Also, the function assumes that the number of rotations is at least 1 and that k is a positive integer. If these conditions are not met, the function might not produce correct results.
"""

