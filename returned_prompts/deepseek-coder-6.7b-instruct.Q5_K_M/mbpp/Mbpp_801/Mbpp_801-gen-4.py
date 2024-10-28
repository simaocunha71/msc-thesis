
def test_three_equal(a, b, c):
  if a==b==c:
    return 3
  elif a==b or b==c or c==a:
    return 2
  else:
    return 0

