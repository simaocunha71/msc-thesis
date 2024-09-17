def pack_consecutive_duplicates(nums: list) -> list:
  if not nums:
    return []
  packed_nums = [[nums[0]]]
  for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
      packed_nums[-1].append(nums[i])
    else:
      packed_nums.append([nums[i]])
  return packed_nums