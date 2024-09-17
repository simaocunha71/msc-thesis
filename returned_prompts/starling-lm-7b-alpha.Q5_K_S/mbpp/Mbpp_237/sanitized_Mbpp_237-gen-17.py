def check_occurences(nums_list: list) -> dict:
  counts = {}
  for i in nums_list:
    if i not in counts:
      counts[i] = 1
    else:
      counts[i] += 1
  return counts