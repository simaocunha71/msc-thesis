def digit_distance_nums(num1: int, num2: int) -> int:
  diff = abs(num1 - num2)
  return sum(int(digit) for digit in str(diff))