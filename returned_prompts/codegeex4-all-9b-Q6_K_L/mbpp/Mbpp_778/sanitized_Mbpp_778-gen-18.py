def pack_consecutive_duplicates(nums: list) -> list:
    result = []
    sub_list = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            sub_list.append(nums[i])
        else:
            result.append(sub_list)
            sub_list = [nums[i]]
    result.append(sub_list)
    return result