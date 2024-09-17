def odd_length_sum(nums: list) -> int:
  result = 0
  for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
      result += sum(nums[i:j])
  return result