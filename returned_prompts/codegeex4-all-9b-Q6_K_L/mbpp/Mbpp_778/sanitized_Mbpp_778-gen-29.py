def pack_consecutive_duplicates(nums: list) -> list:
  result = []
  current = [nums[0]]
  for num in nums[1:]:
      if num == current[-1]:
          current.append(num)
      else:
          result.append(current)
          current = [num]
  result.append(current)
  return result