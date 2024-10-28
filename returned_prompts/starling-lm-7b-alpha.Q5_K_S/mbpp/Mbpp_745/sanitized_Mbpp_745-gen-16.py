def divisible_by_digits(startnum: int,endnum: int):
  result = []
  for i in range(startnum, endnum + 1):
    if all(i % j == 0 for j in str(i)):
      result.append(i)
  return result