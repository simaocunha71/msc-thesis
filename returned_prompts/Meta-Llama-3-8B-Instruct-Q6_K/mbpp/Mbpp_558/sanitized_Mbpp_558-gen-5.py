def digit_distance_nums(num1, num2):
  return sum(abs(int(x) - int(y)) for x, y in zip(str(num1), str(num2))) if len(str(num1)) == len(str(num2)) else None