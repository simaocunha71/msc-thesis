
def divisible_by_digits(startnum: int,endnum: int) -> list:
  divisible_nums = []
  for i in range(startnum,endnum+1):
    if all(i%j == 0 for j in str(i)):
      divisible_nums.append(i)
  return divisible_nums


