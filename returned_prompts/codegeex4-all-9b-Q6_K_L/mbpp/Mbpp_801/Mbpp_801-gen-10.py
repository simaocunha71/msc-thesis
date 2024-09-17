def test_three_equal(a: int, b: int, c: int) -> int:
  count = 0
  if a == b and b == c:
    count = 3
  elif a == b or b == c or a == c:
    count = 2
  else:
    count = 0
  return count

