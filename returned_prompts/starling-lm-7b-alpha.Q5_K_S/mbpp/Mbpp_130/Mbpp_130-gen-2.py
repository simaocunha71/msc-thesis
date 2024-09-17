
def max_occurrences(nums: list) -> int:
  nums_dict = {}
  for i in nums:
    if i in nums_dict:
      nums_dict[i] += 1
    else:
      nums_dict[i] = 1
  max_val = max(nums_dict.values())
  for i in nums_dict:
    if nums_dict[i] == max_val:
      return i


