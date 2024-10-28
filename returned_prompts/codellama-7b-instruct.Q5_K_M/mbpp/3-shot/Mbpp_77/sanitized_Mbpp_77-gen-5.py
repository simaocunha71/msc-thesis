def is_Diff(num):
  sum = 0
  while num > 0:
    sum += num % 10
    num = num // 10
  return sum % 11 == 0