"""
Here's a step-by-step guide on how to approach this problem:

1. To solve this problem, we need to find the maximum sum of the sub-array in the repeated array.
2. We know that the maximum sum of a sub-array can be found using Kadane's algorithm.
3. We can apply Kadane's algorithm on the given array as well as the repeated array.
4. The maximum sum of the given array will be multiplied by k to find the maximum sum of the repeated array.
5. Finally, we need to compare the maximum sum of the given array and the repeated array to find the largest sum.

Here's the Python code to implement this approach:
"""
def max_sub_array_sum_repeated(nums, k, n):
    # Applying Kadane's algorithm on the given array
    max_sum = float("-inf")
    curr_sum = 0
    for num in nums:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)

    # Applying Kadane's algorithm on the repeated array
    max_sum_repeated = float("-inf")
    curr_sum_repeated = 0
    for _ in range(k):
        for num in nums:
            curr_sum_repeated = max(num, curr_sum_repeated + num)
            max_sum_repeated = max(max_sum_repeated, curr_sum_repeated)

    # Comparing the maximum sum of the given array and the repeated array
    return max(max_sum, max_sum_repeated)

# Testing the function
print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3))  # Output: 30

```
  
This function first applies Kadane's algorithm on the given array to find the maximum sum of the sub-array. Then, it applies Kadane's algorithm on the repeated array (by multiplying each element of the given array by k). Finally, it compares the maximum sum of the given array and the repeated