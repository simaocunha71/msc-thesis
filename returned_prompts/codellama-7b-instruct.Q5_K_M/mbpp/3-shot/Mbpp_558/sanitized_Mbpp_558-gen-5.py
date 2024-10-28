def digit_distance_nums(num1: int,num2: int) -> int:
  num1_list = list(str(num1))
  num2_list = list(str(num2))
  sum = 0
  for i in range(len(num1_list)):
    sum += abs(int(num1_list[i]) - int(num2_list[i]))
  return sum