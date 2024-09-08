def find_Max_Num(nums):
    str_nums = [str(i) for i in nums]
    str_nums.sort(reverse=True)
    return int(''.join(str_nums))