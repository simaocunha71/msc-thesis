def freq_count(nums:list)->dict:
  return {i:nums.count(i) for i in nums}