"""
def max_occurrences(nums):
    counts = {}
    for i in nums:
        if i not in counts:
            counts[i] = 0
        counts[i] += 1
    max_count = 0
    max_item = None
    for i in counts:
        if counts[i] > max_count:
            max_count = counts[i]
            max_item = i
    return max_item

nums = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]
print(max_occurrences(nums)) # 2
"""

def max_occurrences(nums):
    return max(set(nums), key = nums.count)

nums = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]
print(max_occurrences(nums)) # 2


