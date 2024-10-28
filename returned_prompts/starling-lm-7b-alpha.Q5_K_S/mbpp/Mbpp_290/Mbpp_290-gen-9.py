
def max_length(nums: list) -> tuple:
  max_length = max(len(i) for i in nums)
  return max_length, [i for i in nums if len(i) == max_length][0]


