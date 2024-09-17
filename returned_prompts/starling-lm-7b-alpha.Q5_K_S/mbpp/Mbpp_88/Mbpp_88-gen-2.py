
def freq_count(nums: list) -> dict:
  freq_dict = {}
  for num in nums:
    if num not in freq_dict:
      freq_dict[num] = 1
    else:
      freq_dict[num] += 1
  return freq_dict


