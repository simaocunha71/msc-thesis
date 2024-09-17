def is_Monotonic(nums):
    inc_flag = False
    dec_flag = False
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            inc_flag = True
        elif nums[i] > nums[i+1]:
            dec_flag = True
    if inc_flag and dec_flag:
        return False
    else:
        return True