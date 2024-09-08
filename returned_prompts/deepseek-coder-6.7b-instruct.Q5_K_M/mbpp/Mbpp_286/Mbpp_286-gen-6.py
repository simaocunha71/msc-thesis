This problem can be solved by understanding that the maximum subarray sum is not affected by the repetition of the array. 
So we can solve it by finding the maximum subarray sum for the original array and then multiply it by k.

Here is the Python code for the above solution.

```python
def kadane(arr):
    max_current = max_global = arr[0]
    for i in range(1,len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    return max_global

def max_sub_array_sum_repeated(arr, k):
    return kadane(arr) * k

print(max_sub_array_sum_repeated([10, 20, -30, -1], 4))
```

This code works by first using the Kadane's algorithm to find the maximum subarray sum in the original array. Then, it simply multiplies this sum by k. 
The function kadane returns the maximum subarray sum in linear time.
"""

