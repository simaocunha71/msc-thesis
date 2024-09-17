from itertools import combinations
def find_Odd_Pair(nums, target):
    result = 0
    for i in range(len(nums)):
        for comb in combinations(nums,r=2):
            if get_xor(comb) == 1:
                result += 1
    return result