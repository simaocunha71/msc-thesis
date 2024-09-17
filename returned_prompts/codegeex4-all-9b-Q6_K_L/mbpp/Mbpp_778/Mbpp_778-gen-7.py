def pack_consecutive_duplicates(nums: list) -> list:
  output = []
  sub_list = [nums[0]]
  for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
      sub_list.append(nums[i])
    else:
      output.append(sub_list)
      sub_list = [nums[i]]
  output.append(sub_list)
  return output

