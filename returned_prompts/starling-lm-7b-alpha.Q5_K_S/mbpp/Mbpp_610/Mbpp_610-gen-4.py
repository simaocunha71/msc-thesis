
def remove_kth_element(nums,k):
  if k > len(nums):
    return nums
  return nums[:k] + nums[k+1:]


