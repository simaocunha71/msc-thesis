
def divisible_by_digits(startnum, endnum):
  divisible_nums = []
  for n in range(startnum, endnum+1):
    if all(n % i == 0 for i in str(n)):
      divisible_nums.append(n)
  return divisible_nums


