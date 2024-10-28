def check_occurences(nums:list):
  result = {}
  for i in range(len(nums)):
    if nums[i] in result:
      result[nums[i]] += 1
    else:
      result[nums[i]] = 1
  return result