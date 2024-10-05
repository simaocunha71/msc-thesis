
    min_sum = float('inf')
    cur_sum = 0

    for num in nums:
        cur_sum += num
        min_sum = min(min_sum, cur_sum)
        if cur_sum > 0:
            cur_sum = 0

    return min_sum if min_sum != float('inf') else max(nums)

print(minSubArraySum([2, 3, -4, 1, -2, 4]))  # 1
print(minSubArraySum([-1, -2, -3]))  # -6
print(minSubArraySum([1, 2, 3]))  # 1
print(minSubArraySum([-1, 2, 3]))  # -1
<jupyter_output>
1
-6
1
-1
<jupyter_text>
Problem 10: 3Sum ProblemGiven an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.Note: The solution set must not contain duplicate triplets. Example:Given array nums = [-1, 0, 1, 2, -1, -4],A solution set is:[  [-1, 0, 1],  [-1, -1, 2]]
<jupyter_code>
