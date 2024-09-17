def freq_count(nums):
  count_dict = {}
  for num in nums:
    if num in count_dict:
      count_dict[num] += 1
    else:
      count_dict[num] = 1
  return count_dict