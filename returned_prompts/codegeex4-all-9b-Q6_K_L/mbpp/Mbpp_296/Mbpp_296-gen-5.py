def get_Inv_Count(nums):
    # create a copy of the list
    temp = nums[:]
    inv_count = 0
    # sort the list
    nums.sort()
    # find the index of each element in the sorted list
    for i in range(len(temp)):
        inv_count += nums.index(temp[i])
        nums.remove(temp[i])
    return inv_count

