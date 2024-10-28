def max_occurrences(nums: list) -> int:
  count_dict = {}
  for num in nums:
    if num in count_dict:
      count_dict[num] += 1
    else:
      count_dict[num] = 1
  max_occurrence = max(count_dict.values())
  max_num = [k for k, v in count_dict.items() if v == max_occurrence]
  if len(max_num) == 1:
    return max_num[0]
  else:
    return max_num