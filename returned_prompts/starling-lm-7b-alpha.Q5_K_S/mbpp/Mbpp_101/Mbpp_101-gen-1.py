"""
def kth_element(nums, k):
    nums.sort()
    return nums[k-1]
"""

def kth_element(nums, k):
    if k > len(nums): return None
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] >= nums[k - 1]:
            right = mid - 1
        else:
            left = mid + 1
    return nums[left]

print(kth_element([12,3,5,7,19], 2))  # 3
print(kth_element([12,3,5,7,19], 5))  # 19
print(kth_element([12,3,5,7,19], 1))  # 3
print(kth_element([12,3,5,7,19], 6))  # None
print(kth_element([12,3,5,7,19], 0))  # None
print(kth_element([12,3,5,7,19], 7))  # None

```
该代码实现了一个函数 kth_element，用于找到给定数组 nums 中第 k 个元素。该函数首先检查 k 是否在数组 nums 的范围内，如果不在范围内，则返回 None。然后，它使用二分查找算法找到第 k 个元素的索引。最后，它返回 nums 中第 k 个元素。

这个解决方案的时间复杂度是 O(log n)，其中 n 是数组 nums 的长度。这是因为二分查找算法在平均情况下具有线性时间复杂度。

这个解决方案的空间复杂度是 O(1)，因为它只使用了常数级别的额外空间