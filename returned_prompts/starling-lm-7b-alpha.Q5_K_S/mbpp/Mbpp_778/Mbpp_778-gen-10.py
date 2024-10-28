
def pack_consecutive_duplicates(nums:list) -> list:
  packed_nums = []
  for i in range(len(nums)):
    if i == 0 or nums[i] != nums[i-1]:
      packed_nums.append([nums[i]])
    else:
      packed_nums[-1].append(nums[i])
  return packed_nums


