def digit_distance_nums(num1,num2):
  num1_digits = [int(digit) for digit in str(num1)]
  num2_digits = [int(digit) for digit in str(num2)]
  digit_diff = [abs(num1_digit - num2_digit) for num1_digit, num2_digit in zip(num1_digits, num2_digits)]
  return sum(digit_diff)