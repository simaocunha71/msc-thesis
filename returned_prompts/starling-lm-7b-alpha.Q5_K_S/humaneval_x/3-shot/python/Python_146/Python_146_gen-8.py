    count = 0
    for i in range(len(nums)):
        if int(str(nums[i])) > 10 and (nums[i] % 2 != 0):
            count += 1

    return count


