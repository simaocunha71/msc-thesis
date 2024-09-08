def find_Max_Num(nums):
    nums_str = [str(num) for num in nums]
    nums_str.sort(reverse=True)
    return int(''.join(nums_str))