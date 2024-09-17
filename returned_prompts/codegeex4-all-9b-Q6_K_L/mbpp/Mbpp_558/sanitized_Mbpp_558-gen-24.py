def digit_distance_nums(num1, num2):
  return abs(sum(int(digit) for digit in str(num1)) - sum(int(digit) for digit in str(num2)))