
def d(n):
  return sum([i for i in range(1, n) if n % i == 0])

def amicable_numbers_sum(limit):
  result = 0
  for i in range(1, limit+1):
    if i != d(i) and i == d(d(i)):
      result += i
  return result


