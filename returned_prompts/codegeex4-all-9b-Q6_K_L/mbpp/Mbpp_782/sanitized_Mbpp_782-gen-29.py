def odd_length_sum(nums: list) -> int:
  total_sum = 0
  for i in range(len(nums)):
    for j in range(i, len(nums), 2):
      subarray = nums[i:j+1]
      total_sum += sum(subarray)
  return total_sum