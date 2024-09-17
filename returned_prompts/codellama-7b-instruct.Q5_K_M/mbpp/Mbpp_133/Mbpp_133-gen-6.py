
def sum_negativenum(numbers):
  negativesum = 0
  for num in numbers:
    if num < 0:
      negativesum += num
  return negativesum


