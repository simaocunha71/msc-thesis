def armstrong_number(num: int) -> bool:
  total = 0
  temp = num
  while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10
  return total == num


