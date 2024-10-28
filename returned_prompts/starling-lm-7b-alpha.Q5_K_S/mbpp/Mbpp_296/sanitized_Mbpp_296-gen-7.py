def get_Inv_Count(nums):
    i = 0
    count = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if nums[i] > nums[j]:
                count += 1
            j += 1
        i += 1
    return count
nums = [1,20,6,4,5]