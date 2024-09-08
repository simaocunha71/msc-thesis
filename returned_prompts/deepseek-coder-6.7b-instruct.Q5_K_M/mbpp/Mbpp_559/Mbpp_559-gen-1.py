"""
The idea is to use Kadane's algorithm. It is a dynamic programming algorithm.

The function works by initializing a variable max_current to hold the maximum sum of the subarray ending at the current position. It also initializes a variable max_global to hold the maximum sum of the subarray seen so far.

For each element in the list, we update max_current to be the maximum of the current element and the sum of the current element and the previous max_current. If max_current is greater than max_global, we update max_global.

Finally, we return max_global.
"""

def max_sub_array_sum(arr, n):
    max_current = arr[0]
    max_global = arr[0]

    for i in range(1, n):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current

    return max_global

print(max_sub_array_sum([-2, -3, 4, -1, -2, 1, 5, -3], 8))  # 7
"""
The function works by starting from the first element and iterating through the list. On each iteration, it updates the maximum sum of the subarray ending at the current position by comparing the current element with the sum of the current element and the previous maximum sum. If the current element is larger, it updates the maximum sum. It then checks if the maximum sum so far is larger than the global maximum sum and updates the global maximum sum if it is. Finally, it returns the global maximum sum.
"""

# This function also works on negative numbers as it will not consider the subarray if the sum becomes negative. The maximum subarray sum is the maximum sum of the subarray ending at the current position.
<jupyter_output>
7
<jupyter_text>
**Problem 2**
<jupyter_code>
