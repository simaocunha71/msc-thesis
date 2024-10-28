def reverse_Array_Upto_K(nums: list,k: int) -> list:
  nums[:k] = nums[:k][::-1]
  return nums

