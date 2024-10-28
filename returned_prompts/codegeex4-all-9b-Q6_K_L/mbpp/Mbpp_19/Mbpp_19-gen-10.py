def test_duplicate(nums: list):
  if len(nums) != len(set(nums)):
    return True
  return False