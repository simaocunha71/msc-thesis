def check_Consecutive(nums: list) -> bool:
  sorted_nums = sorted(nums)
  return all(sorted_nums[i] + 1 == sorted_nums[i + 1] for i in range(len(sorted_nums) - 1))