def zero_count(nums:list):
  zero_count = len([x for x in nums if x==0])
  return zero_count/len(nums)