
def remove_kth_element(nums: list, k: int) -> list:
  nums_len = len(nums)
  if k > nums_len:
    return nums
  return nums[:k] + nums[k + 1:]


