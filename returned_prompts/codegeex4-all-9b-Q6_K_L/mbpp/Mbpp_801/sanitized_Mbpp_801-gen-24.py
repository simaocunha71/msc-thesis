def test_three_equal(num1, num2, num3):
  return sum(1 for num in (num1, num2, num3) if num == num1)