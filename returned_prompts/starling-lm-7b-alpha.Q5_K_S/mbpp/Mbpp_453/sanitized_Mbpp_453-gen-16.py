def sumofFactors(num:int):
  factors = []
  for i in range(1,num+1):
    if num%i==0:
      factors.append(i)
  even_sum = sum(filter(lambda x: x%2 == 0, factors))
  return even_sum