def odd_length_sum(nums: list) -> int:
  total = 0
  for i in range(len(nums)):
    for j in range(i, len(nums), 2):
      total += sum(nums[i:j+1])
  return total

