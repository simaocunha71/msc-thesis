def pack_consecutive_duplicates(nums: list) -> list:
  result = []
  curr = []
  for i, n in enumerate(nums):
    if i == 0 or n != nums[i - 1]:
      curr = [n]
    else:
      curr.append(n)
    if i + 1 == len(nums) or nums[i + 1] != n:
      result.append(curr)
  return result