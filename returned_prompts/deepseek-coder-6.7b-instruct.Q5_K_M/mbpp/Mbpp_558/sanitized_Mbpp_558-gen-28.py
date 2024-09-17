def digit_distance_nums(num1, num2):
  num1, num2 = str(num1), str(num2)
  return sum(abs(int(x) - int(y)) for x, y in zip(num1, num2))