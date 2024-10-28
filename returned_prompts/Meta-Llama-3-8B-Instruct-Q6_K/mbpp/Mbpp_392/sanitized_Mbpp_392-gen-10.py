def get_max_sum(n):
  memo = {1: 1}
  def f(n):
    if n in memo:
      return memo[n]
    if n < 1:
      return 0
    max_sum = 0
    for i in range(2, 6):
      if n % i == 0:
        max_sum = max(max_sum, f(n//i) + n)
    memo[n] = max_sum
    return max_sum
  return f(n)  # returns 106 for n = 60