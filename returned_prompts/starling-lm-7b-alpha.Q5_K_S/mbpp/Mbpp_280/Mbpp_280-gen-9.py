
def sequential_search(nums: list,target: int) -> tuple:
  for i,num in enumerate(nums):
    if num == target:
      return (True, i)
  return (False, -1)


