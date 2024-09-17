def Find_Min(nums: list) -> list:
  min_len = min(len(i) for i in nums)
  return [num for num in nums if len(num) == min_len][0]