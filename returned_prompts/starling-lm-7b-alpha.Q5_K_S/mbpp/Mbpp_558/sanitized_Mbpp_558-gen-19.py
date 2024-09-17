def digit_distance_nums(num1: int,num2: int) -> int:
  num1_str = str(num1)
  num2_str = str(num2)
  if len(num1_str) != len(num2_str):
    raise ValueError("The length of two numbers should be equal")
  distance_sum = 0
  for i in range(len(num1_str)):
    distance_sum += abs(int(num1_str[i]) - int(num2_str[i]))
  return distance_sum