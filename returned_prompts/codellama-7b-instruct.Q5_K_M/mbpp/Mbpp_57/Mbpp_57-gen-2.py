
def find_Max_Num(digits: list) -> int:
  digits.sort(reverse=True)
  num = ''
  for i in digits:
    num += str(i)
  return int(num)


