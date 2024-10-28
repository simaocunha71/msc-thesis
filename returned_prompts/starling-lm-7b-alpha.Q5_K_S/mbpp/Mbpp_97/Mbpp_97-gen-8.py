
def frequency_lists(nums: list) -> dict:
  return {num: nums.count(num) for num in set(nums)}


