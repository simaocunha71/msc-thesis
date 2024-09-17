def consecutive_duplicates(nums: list) -> list:
  res = []
  for i in range(len(nums)):
    if i == 0 or nums[i] != nums[i-1]:
      res.append(nums[i])
  return res