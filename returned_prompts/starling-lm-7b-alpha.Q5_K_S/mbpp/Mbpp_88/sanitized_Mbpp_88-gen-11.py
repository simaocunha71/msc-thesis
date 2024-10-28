def freq_count(nums: list) -> dict:
  return {num:nums.count(num) for num in nums}