def remove_kth_element(nums: list, k: int) -> list:
  if k > len(nums):
    return nums
  return nums[:k] + nums[k+1:]