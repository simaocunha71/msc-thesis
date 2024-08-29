"""
def get_pairs_count(nums, sum):
    count = 0
    nums_dict = {}
    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1
    for num in nums_dict:
        if sum-num in nums_dict:
            if num != sum-num:
                count += nums_dict[num]*nums_dict[sum-num]
            else:
                count += nums_dict[num]*(nums_dict[num]-1)
    return count//2
print(get_pairs_count([1,1,1,1],2))
"""

