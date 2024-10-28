
def armstrong_number(num: int):
  sum_of_digits = 0
  temp = num
  while temp > 0:
    digit = temp % 10
    sum_of_digits += digit ** len(str(num))
    temp //= 10
  return sum_of_digits == num


