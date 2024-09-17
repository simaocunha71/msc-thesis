def validate(num):
  num = str(num)
  return all(int(digit) >= num.count(digit) for digit in num)