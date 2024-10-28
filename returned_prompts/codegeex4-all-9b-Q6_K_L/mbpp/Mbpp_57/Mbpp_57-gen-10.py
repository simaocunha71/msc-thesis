def find_Max_Num(nums):
    return int(''.join(map(str, sorted(nums, reverse=True))))