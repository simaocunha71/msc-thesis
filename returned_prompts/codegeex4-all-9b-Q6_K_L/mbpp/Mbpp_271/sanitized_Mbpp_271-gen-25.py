def even_Power_Sum(n):
  even_nums = []
  for i in range(2, 2*n+1, 2):
    even_nums.append(i**5)
  return sum(even_nums)