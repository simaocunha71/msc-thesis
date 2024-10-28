def divisible_by_digits(startnum,endnum):
  res = []
  for i in range(startnum, endnum + 1):
    digits = str(i)
    for digit in digits:
      if i % int(digit) != 0:
        break
    else:
      res.append(i)
  return res