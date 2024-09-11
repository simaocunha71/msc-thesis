```
def max_sub_array_sum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    if not nums:
        return 0

    curr, res = 0, 0
    for i in xrange(len(nums)):
        if i < k:
            curr = sum(nums[i:i + k])
        else:
            curr = curr + nums[i] - nums[i - k]
        res = max(res, curr)

    return res
```

Explanation:
The problem asks to find the largest sum of a sublist of length k, which can be found using Kadane's algorithm.

The algorithm works by keeping a running total of the subarray sums. It starts by initializing the current sum to the first k elements of the array. Then, it iterates through the array, adding each element to the current sum until it exceeds k. Once the current sum exceeds k, it subtracts the oldest element from the current sum and adds the newest element. This process is repeated until the end of the array is reached.

The algorithm maintains two variables: curr and res. curr keeps track of the sum of the current subarray, while res keeps track of the maximum sum found so far. At each step, the algorithm updates res to be the maximum of res and curr, ensuring that res always holds the maximum sum found.

The algorithm returns the maximum sum found, which is stored in res.

The time complexity of the algorithm is O(n), where n is the length of the input array. The algorithm iterates through the array exactly once, performing constant time operations at each step.

Overall, the algorithm efficiently finds the maximum sum of a sublist of length k in the given list, as required by the problem statement.

The algorithm is implemented in the max_sub_array_sum function, which takes in the input array nums and the length of the sublist k as arguments. The function returns the maximum sum found by the algorithm.

The function first checks if the input array is empty and returns 0 in that case. This is done to handle the edge case where no sublist of length k exists