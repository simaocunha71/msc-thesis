
def odd_length_sum(nums: list) -> int:
  result = 0
  for i in range(len(nums)):
    result += (2*len(nums)-1)*nums[i]
  return result


