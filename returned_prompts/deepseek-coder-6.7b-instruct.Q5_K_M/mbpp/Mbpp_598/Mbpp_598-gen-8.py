
def armstrong_number(num):
  sum = 0
  temp = num
  while temp > 0:
    digit = temp % 10
    sum += digit ** 03
    temp //= 10
  return num == sum

