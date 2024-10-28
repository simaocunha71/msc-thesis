def consecutive_duplicates(nums: list) -> list:
  final_nums = []
  for num in nums:
    if len(final_nums) == 0 or num != final_nums[-1]:
      final_nums.append(num)
  return final_nums


