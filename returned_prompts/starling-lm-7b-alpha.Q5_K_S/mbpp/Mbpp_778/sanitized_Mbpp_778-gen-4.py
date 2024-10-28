def pack_consecutive_duplicates(nums):
    lst = []
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            lst.append([nums[i]])
        else:
            lst[len(lst)-1].append(nums[i])
    return lst