def pack_consecutive_duplicates(nums: list) -> list:
  output = []
  for num in nums:
    if not output or output[-1][0] != num:
      output.append([num])
    else:
      output[-1].append(num)
  return output

