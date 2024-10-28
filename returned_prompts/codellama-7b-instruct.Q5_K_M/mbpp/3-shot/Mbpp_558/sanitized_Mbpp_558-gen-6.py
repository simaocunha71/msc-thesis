def digit_distance_nums(num1: int,num2: int) -> int:
  sum_diff = 0
  for digit_num1 in str(num1):
    for digit_num2 in str(num2):
      sum_diff += abs(int(digit_num1) - int(digit_num2))
  return sum_diff