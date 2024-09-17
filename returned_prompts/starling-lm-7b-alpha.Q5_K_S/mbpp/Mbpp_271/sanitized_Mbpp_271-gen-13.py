def even_Power_Sum(n: int) -> int:
  sum_list = []
  for i in range(n+1):
    sum_list.append(i**5)
  return sum(sum_list[0:n])