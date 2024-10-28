
def sum(num1: int, num2: int) -> int:
  common_divisors = []
  for i in range(1,min(num1, num2)+1):
    if num1 % i == 0 and num2 % i == 0:
      common_divisors.append(i)
  return sum(common_divisors)


