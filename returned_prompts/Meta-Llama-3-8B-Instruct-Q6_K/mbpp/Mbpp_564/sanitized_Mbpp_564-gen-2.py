def count_Pairs(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] != nums[j]:
                count += 1
                if count == k:
                    return
    return count