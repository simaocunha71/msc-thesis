
def test_duplicate(nums: list) -> bool:
  if len(nums) == len(set(nums)):
    return False
  else:
    return True


