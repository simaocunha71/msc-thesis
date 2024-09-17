
def second_smallest(nums:list)->int:
  if len(nums) < 2:
    raise ValueError("List must have at least two elements")
  smallest = min(nums)
  return min(x for x in nums if x != smallest)


