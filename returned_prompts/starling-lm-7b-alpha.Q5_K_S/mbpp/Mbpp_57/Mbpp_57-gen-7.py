
def find_Max_Num(nums):
    nums.sort(reverse=True)
    max_num = 0
    for i in nums:
        max_num = max_num * 10 + i
    return max_num


