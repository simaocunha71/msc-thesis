
def sum_of_digits(my_list):
  sums = []
  for num in my_list:
    sum = 0
    while num > 0:
      sum += num % 10
      num //= 10
    sums.append(sum)
  return sums


