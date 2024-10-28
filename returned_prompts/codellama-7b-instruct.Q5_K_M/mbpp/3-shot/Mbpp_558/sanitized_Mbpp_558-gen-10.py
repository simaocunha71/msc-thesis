def digit_distance_nums(num1: int, num2: int) -> int:
  distance = 0
  for i in range(len(str(abs(num1 - num2)))):
    distance += 1
  return distance