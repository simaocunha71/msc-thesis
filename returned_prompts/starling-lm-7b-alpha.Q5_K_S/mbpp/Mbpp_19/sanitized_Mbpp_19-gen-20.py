def test_duplicate(nums:list)->bool:
  if len(set(nums)) == len(nums):
    return False
  else:
    return True