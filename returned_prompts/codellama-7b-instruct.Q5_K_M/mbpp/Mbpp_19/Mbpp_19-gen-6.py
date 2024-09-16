
import collections

def test_duplicate(nums):
    return len(nums) != len(set(nums))

# 排序后判断相邻两个数字是否相同


def test_duplicate2(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

# 使用字典


def test_duplicate3(nums):
    return len(nums) != len(set(nums))

# 使用字典 + 排序


def test_duplicate4(nums):
    nums.sort()
    s = set()
    for i in nums:
        if i in s:
            return True
        else:
            s.add(i)
    return False

# 使用列表


def test_duplicate5(nums):
    return len(nums) != len(set(nums))

# 使用列表 + 排序


def test_duplicate6(nums):
    nums.sort()
    l = []
    for i in nums:
        if i in l:
            return True
        else:
            l.append(i)
    return False
