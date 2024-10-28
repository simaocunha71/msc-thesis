def divisible_by_digits(startnum, endnum):
  result = []
  for num in range(startnum, endnum+1):
    if all(num % int(digit) == 0 for digit in str(num) if digit != '0'):
      result.append(num)
  return result