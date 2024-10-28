def test_duplicate(nums: list) -> bool:
  seen = set()
  for num in nums:
    if num in seen:
      return True
    seen.add(num)
  return False