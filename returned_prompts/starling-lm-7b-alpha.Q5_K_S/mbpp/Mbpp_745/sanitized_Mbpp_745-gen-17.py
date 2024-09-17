def divisible_by_digits(startnum: int,endnum: int) -> list:
  numbers = []
  for num in range(startnum, endnum+1):
    digits = str(num)
    flag = True
    for digit in digits:
      if num % int(digit) != 0:
        flag = False
        break
    if flag:
      numbers.append(num)
  return numbers