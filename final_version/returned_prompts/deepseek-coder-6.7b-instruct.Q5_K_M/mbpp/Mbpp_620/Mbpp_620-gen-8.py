
def largest_subset(nums):
    nums.sort()
    dp = [1]*len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

print(largest_subset([1, 3, 6, 13, 17, 18]))


"""
Explanation:
The function works by sorting the list and then applying dynamic programming to keep track of the largest subset ending at each index. It checks each number to see if it divides any of the previous numbers, and if so, it updates the largest subset ending at that index. The maximum of all the subsets is then returned.

For the given list [1, 3, 6, 13, 17, 18], the function would return 4 because the largest subset that satisfies the condition is [1, 3, 6, 18].
"""
<jupyter_output>
4
<jupyter_text>
**Problem 2**Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.An input string is valid if:1. Open brackets must be closed by the same type of brackets.2. Open brackets must be closed in the correct order.
<jupyter_code>
