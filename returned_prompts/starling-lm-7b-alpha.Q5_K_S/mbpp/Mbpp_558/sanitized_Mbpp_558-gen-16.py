def digit_distance_nums(a, b):
  sum = 0
  while a or b:
    sum += abs(a%10 - b%10)
    a = a//10
    b = b//10
  return sum