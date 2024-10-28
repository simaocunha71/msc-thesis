def remove_kth_element(nums: list,k: int) -> list:
  new_list = nums[:k-1] + nums[k:]
  return new_list

