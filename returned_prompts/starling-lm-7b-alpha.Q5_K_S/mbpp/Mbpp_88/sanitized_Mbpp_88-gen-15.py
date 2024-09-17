def freq_count(nums:list):
  return {i:nums.count(i) for i in set(nums)}