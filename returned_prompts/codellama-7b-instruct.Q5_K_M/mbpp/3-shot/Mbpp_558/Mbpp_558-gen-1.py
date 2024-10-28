
def digit_distance_nums(num1: int, num2: int) -> int:
  sum_of_difference = 0
  num1 = str(num1)
  num2 = str(num2)
  for i in range(len(num1)):
    sum_of_difference += abs(int(num1[i]) - int(num2[i]))
  return sum_of_difference


