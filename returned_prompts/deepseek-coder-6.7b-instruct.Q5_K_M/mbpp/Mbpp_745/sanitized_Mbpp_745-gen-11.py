def divisible_by_digits(startnum, endnum):
  res = []
  for num in range(startnum, endnum+1):
    if all(num % int(i) == 0 for i in str(num) if i != '0'):
      res.append(num)
  return res