def find_Odd_Pair(nums, target):
    res = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] ^ nums[j]) % 2 == 1:
                res.append((nums[i], nums[j]))
    return res
nums = [5,4,7,2,1]
target = 5