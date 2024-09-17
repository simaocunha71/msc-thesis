
def amicable_numbers_sum(n: int) -> int:
  def friendly(n: int) -> bool:
    s = sum(divisors(n))
    if s < n and divisors(s)[0] == s: return True
    return False
  
  def divisors(n: int) -> list:
    res = []
    for i in range(1, int(math.sqrt(n))+1):
      if n % i == 0:
        res.append(i)
        if n//i != i:
          res.append(n//i)
    res.sort()
    return res
  
  sum_ = 0
  for i in range(1, n+1):
    if friendly(i): sum_ += i
  return sum_


