def kth_element(nums, k):
    k = k - 1
    return sorted(nums)[k] if k < len(nums) else None