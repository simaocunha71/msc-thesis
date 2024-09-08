def big_diff(nums):
    return max(nums) - min(nums)
print(big_diff([1,2,3,4]))

# Alternative Solution
def big_diff(nums):
    min_num = nums[0]
    max_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return max_num - min_num
print(big_diff([1,2,3,4]))
<jupyter_output>
3
3
<jupyter_text>
Problem 2:**Given a list of integers, return a list of the integers, omitting any that are less than 0.**
<jupyter_code>
