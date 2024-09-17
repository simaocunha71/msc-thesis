def digit_distance_nums(num1: int, num2: int) -> int:
  digit_distance = 0
  while num1 > 0 or num2 > 0:
    digit_distance += abs(num1 % 10 - num2 % 10)
    num1 = num1 // 10
    num2 = num2 // 10
  return digit_distance