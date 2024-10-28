def divisible_by_digits(startnum, endnum):
  res = []
  for num in range(startnum, endnum+1):
    divisible = True
    for digit in str(num):
      if num % int(digit) != 0:
        divisible = False
        break
    if divisible:
      res.append(num)
  return res