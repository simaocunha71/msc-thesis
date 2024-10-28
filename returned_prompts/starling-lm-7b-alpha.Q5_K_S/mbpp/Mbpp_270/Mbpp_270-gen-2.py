
def sum_even_and_even_index(nums: list) -> int:
  sum_even = 0
  for i in range(0,len(nums),2):
    if nums[i] % 2 == 0:
      sum_even += nums[i]
  return sum_even


