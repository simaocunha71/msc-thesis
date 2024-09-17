
def reverse_Array_Upto_K(nums: list,n: int) -> list:
  left = 0
  right = n
  while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
  return nums


