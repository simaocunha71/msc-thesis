def digit_distance_nums(num1: int, num2: int) -> int:
  return abs(sum(int(digit) for digit in str(num1)) - sum(int(digit) for digit in str(num2)))