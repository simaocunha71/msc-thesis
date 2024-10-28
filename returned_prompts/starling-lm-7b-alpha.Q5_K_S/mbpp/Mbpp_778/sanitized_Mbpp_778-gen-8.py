def pack_consecutive_duplicates(nums):
    res = []
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            res.append([nums[i]])
        else:
            res[-1].append(nums[i])
    return res