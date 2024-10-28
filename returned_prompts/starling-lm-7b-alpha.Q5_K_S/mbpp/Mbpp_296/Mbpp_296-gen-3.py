
def get_Inv_Count(nums: list) -> int:
  inversions = 0
  for i in range(len(nums)):
    for j in range(i+1, len(nums)):
      if nums[i] > nums[j]:
        inversions += 1
  return inversions


