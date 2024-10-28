def digit_distance_nums(num1, num2):
  sum_dist = 0
  for i in range(max(len(str(num1)), len(str(num2)))):
    digit1 = str(num1)[:-1*i-1][::-1] if i < len(str(num1)) else '0'
    digit2 = str(num2)[:-1*i-1][::-1] if i < len(str(num2)) else '0'
    sum_dist += abs(int(digit1) - int(digit2))
  return sum_dist