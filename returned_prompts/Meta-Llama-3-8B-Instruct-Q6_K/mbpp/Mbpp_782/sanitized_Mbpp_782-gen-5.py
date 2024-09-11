def odd_length_sum(nums):
  total = 0
  for i in range(len(nums)):
    for j in range(i, len(nums)):
      if (j - i + 1) % 2 != 0:
        total += sum(nums[i:j+1])
  return total