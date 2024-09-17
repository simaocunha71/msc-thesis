def divisible_by_digits(startnum:int, endnum:int)->list:
  result = []
  for num in range(startnum, endnum+1):
    for digit in str(num):
      if num % int(digit) != 0:
        break
    else:
      result.append(num)
  return result