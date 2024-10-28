def find_Odd_Pair(nums):
    nums.sort()
    odd_pair_count = 0
    for i in range(len(nums) - 1):
        while i > 0 and nums[i] == nums[i-1]:
            i -= 1
        for j in range(i+1, len(nums)):
            if nums[i] ^ nums[j] % 2 != 0:
                odd_pair_count += 1
    return odd_pair_count