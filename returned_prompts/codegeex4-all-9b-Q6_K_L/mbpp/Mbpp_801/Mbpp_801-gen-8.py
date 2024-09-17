def test_three_equal(num1, num2, num3):
  if num1 == num2 == num3:
    return 3
  elif num1 == num2 or num2 == num3 or num1 == num3:
    return 2
  else:
    return 0

