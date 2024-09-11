def pack_consecutive_duplicates(nums):
    res, cur = [], []
    for i in nums:
        if cur and cur[-1] == i:
            cur.append(i)
        else:
            if cur:
                res.append(cur)
            cur = [i]
    if cur:
        res.append(cur)
    return res

# Time:  O(n)
# Space: O(n)

# optimized from the original solution
def pack_consecutive_duplicates2(nums):
    res = []
    for i in nums:
        if not res or res[-1][-1] != i:
            res.append([i])
        else:
            res[-1].append(i)
    return res

# Time:  O(n)
# Space: O(n)

# optimized from the original solution
def pack_consecutive_duplicates3(nums):
    res = []
    for i in nums:
        res.append(i) if not res or res[-1] != i else res.pop()
    return res

# Time:  O(n)
# Space: O(1)
"""
def pack_consecutive_duplicates(nums):
    result = []
    cur = []
    for i in nums:
        if not cur or cur[-1] != i:
            cur = [i]
        else:
            cur.append(i)
        if len(cur) >= 2:
            result.append(cur)
            cur = [i]
    if cur:
        result.append(cur)
    return result
"""

"""
def pack_consecutive_duplicates(nums):
    result = []
    for i in nums:
        if not result or result[-1][-1] != i:
            result.append([i])
        else:
            result[-1].append(i)
    return result
"""

"""
def pack_consecutive_duplicates(nums):
    result = []
    for i in nums:
        result