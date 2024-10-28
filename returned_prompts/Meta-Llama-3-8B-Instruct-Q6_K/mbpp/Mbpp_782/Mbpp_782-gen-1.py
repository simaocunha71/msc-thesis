The problem is asking to find the sum of all subarrays with odd length in a given array. 
However, without any additional information, it's not clear what subarrays should be considered. 
Thanks to the provided unit test `assert odd_length_sum([1,2,4]) == 14`, we can infer that the problem intends to consider all possible subarrays of odd length. 

Here's a Python function that solves the problem:

```python
def odd_length_sum(arr):
    total_sum = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            if (j-i)%2 != 0:
                total_sum += sum(arr[i:j])
    return total_sum
```

This function works by iterating over all possible subarrays of the input array, and for each subarray, it checks if the length of the subarray is odd. If it is, it adds the sum of the subarray to the total sum. The result is the sum of all subarrays with odd length. 

Please note that this function has a time complexity of O(n^2), where n is the length of the input array, because it needs to iterate over all possible subarrays. This might be inefficient for large input arrays. If you need a more efficient solution, you might need to use a different approach. 