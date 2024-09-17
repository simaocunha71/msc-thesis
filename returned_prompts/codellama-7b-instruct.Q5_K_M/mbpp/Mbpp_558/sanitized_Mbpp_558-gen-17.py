def digit_distance_nums(num1, num2) -> int:
  num1_digits = [int(i) for i in str(num1)]
  num2_digits = [int(i) for i in str(num2)]
  total = 0
  for i in range(len(num1_digits)):
    total += abs(num1_digits[i] - num2_digits[i])
  return total