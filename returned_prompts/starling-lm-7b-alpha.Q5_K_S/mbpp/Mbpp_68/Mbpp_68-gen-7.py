
def is_Monotonic(nums):
    inc_flag = False
    dec_flag = False
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            inc_flag = True
        if nums[i] > nums[i+1]:
            dec_flag = True
    if inc_flag and not dec_flag:
        return True
    elif not inc_flag and dec_flag:
        return True
    else:
        return False


