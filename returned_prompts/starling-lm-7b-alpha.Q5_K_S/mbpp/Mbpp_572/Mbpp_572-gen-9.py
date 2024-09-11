"""
def two_unique_nums(nums):
    res = []
    for num in nums:
        if num not in res:
            res.append(num)
    return res

print(two_unique_nums([1,2,3,2,3,4,5]))

"""

def two_unique_nums(nums):
    return list(set(nums))

print(two_unique_nums([1,2,3,2,3,4,5]))




















"""
def two_unique_nums(nums):
    res = []
    for num in nums:
        if num not in res:
            res.append(num)
    return res

print(two_unique_nums([1,2,3,2,3,4,5]))
"""


```
def two_unique_nums(nums):
    res = set()
    for num in nums:
        if num not in res:
            res.add(num)
    return list(res)

print(two_unique_nums([1,2,3,2,3,4,5]))
```