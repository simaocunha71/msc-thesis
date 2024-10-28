def sum(num1, num2):
  if num1 > num2:
    num1, num2 = num2, num1
  sum_div = 0
  for i in range(1, num1+1):
    if num1 % i == 0 and num2 % i == 0:
      sum_div += i
  return sum_div