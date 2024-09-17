def odd_length_sum(nums: list) -> int:
  res = 0
  for i in range(len(nums)):
    for j in range(i, len(nums), 2):
      res += sum(nums[i:j+1])
  return res