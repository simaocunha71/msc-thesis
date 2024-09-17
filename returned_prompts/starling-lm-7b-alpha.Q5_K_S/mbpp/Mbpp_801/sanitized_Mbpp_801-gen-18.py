def test_three_equal(a: int, b: int, c: int) -> int:
  count = 0
  if a == b:
    count += 1
  if b == c:
    count += 1
  if c == a:
    count += 1
  return count