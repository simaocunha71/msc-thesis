
def digit_distance_nums(num1: int, num2: int) -> int:
  num1 = str(num1)
  num2 = str(num2)
  if len(num1) != len(num2):
    raise ValueError('Two numbers must be of equal length')
  distance = 0
  for i in range(len(num1)):
    distance += abs(int(num1[i]) - int(num2[i]))
  return distance


