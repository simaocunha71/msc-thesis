def divisible_by_digits(startnum: int, endnum: int) -> list:
  result = []
  for i in range(startnum, endnum + 1):
    digits_sum = 0
    for digit in str(i):
      digits_sum += int(digit)
    if digits_sum == 0:
      result.append(i)
  return result