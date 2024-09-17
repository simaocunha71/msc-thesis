
def odd_length_sum(nums):
    ans = 0
    for i in range(len(nums)):
        ans += sum(nums[j] for j in range(i, len(nums), 2))
    return ans


