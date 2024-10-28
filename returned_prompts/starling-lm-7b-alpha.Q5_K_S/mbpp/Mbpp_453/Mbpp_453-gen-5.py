
def sumofFactors(num:int):
  factors = []
  for i in range(1,num+1):
    if num%i == 0:
      factors.append(i)
  even_factors = [i for i in factors if i % 2 == 0]
  return sum(even_factors)


