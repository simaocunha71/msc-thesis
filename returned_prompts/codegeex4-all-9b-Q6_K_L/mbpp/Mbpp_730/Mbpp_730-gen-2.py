def consecutive_duplicates(nums: list) -> list:
  unique_nums = []
  for num in nums:
    if len(unique_nums) == 0 or num != unique_nums[-1]:
      unique_nums.append(num)
  return unique_nums

