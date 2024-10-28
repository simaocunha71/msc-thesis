def pack_consecutive_duplicates(nums: list) -> list:
  grouped_nums = []
  temp = [nums[0]]
  for num in nums[1:]:
    if num != temp[-1]:
      grouped_nums.append(temp)
      temp = [num]
    else:
      temp.append(num)
  grouped_nums.append(temp)
  return grouped_nums

