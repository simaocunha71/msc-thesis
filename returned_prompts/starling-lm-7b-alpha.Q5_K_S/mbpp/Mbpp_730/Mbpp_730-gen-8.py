
def consecutive_duplicates(nums: list) -> list:
  result = []
  for i in range(len(nums)):
    if i == 0 or nums[i] != nums[i-1]:
      result.append(nums[i])
  return result


