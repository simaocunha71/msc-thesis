def pancake_sort(nums: list):
    for i in range(len(nums)):
        max_ind = i
        for j in range(i, len(nums)):
            if nums[j] > nums[max_ind]:
                max_ind = j
        nums.insert(i, nums.pop(max_ind))
    return nums