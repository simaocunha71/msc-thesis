def test_duplicate(arr: list) -> bool:
  return len(arr) != len(set(arr))