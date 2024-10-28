def reverse_Array_Upto_K(nums: list, k: int) -> list:
  nums[:k+1] = nums[:k+1][::-1]
  return nums