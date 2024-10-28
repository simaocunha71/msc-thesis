
def test_three_equal(num1, num2, num3):
  if num1 == num2 and num2 == num3:
    return 3
  elif num1 == num2 and num2 != num3:
    return 2
  elif num1 == num3 and num2 != num3:
    return 2
  elif num2 == num3 and num1 != num3:
    return 2
  elif num1 != num2 and num2 != num3 and num1 != num3:
    return 0


