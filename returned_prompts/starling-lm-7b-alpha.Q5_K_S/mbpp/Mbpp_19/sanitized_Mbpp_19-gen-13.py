def test_duplicate(nums: list) -> bool:
  return len(set(nums)) != len(nums)