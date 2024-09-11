"""
def find_Odd_Pair(nums, target):
    ret = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i] ^ nums[j]) % 2 == 1:
                ret += 1
    return ret

nums = [5,4,7,2,1]
target = 5
print(find_Odd_Pair(nums,target))
"""

def find_Odd_Pair(nums, target):
    ret = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i] ^ nums[j]) % 2 == 1:
                ret += 1
    return ret

nums = [5,4,7,2,1]
target = 5
print(find_Odd_Pair(nums,target))


```