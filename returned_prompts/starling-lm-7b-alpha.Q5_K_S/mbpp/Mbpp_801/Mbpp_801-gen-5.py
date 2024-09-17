
def test_three_equal(x,y,z):
  if x == y and y == z:
    return 3
  elif x == y or y == z:
    return 2
  elif x == z:
    return 2
  else:
    return 0


