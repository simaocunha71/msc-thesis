def freq_count(nums: list) -> dict:
  return dict(fromkeys(nums, 0).update(dict(zip(nums, [i for i in nums]))))