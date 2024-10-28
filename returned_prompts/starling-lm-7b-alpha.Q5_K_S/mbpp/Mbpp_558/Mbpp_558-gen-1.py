
def digit_distance_nums(num1: int, num2: int) -> int:
  num1_digit = len(str(num1))
  num2_digit = len(str(num2))
  if num1_digit < num2_digit:
    num1_digit += 1
  elif num2_digit < num1_digit:
    num2_digit += 1
  diff_nums = [abs(int(str(num1)[i]) - int(str(num2)[i])) for i in range(num1_digit)]
  return sum(diff_nums)


