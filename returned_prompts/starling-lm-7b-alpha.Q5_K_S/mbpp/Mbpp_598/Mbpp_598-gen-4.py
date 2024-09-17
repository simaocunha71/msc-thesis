
def armstrong_number(num):
  total = 0
  temp = num
  while temp > 0:
    digit = temp % 10
    total += digit ** len(str(num))
    temp //= 10
  return num == total


