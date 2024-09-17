
def remove_kth_element(nums: list, k: int) -> list:
  return nums[:k] + nums[k + 1:]


