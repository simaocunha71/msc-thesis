def get_max_sum(n: int) -> int:
  memo = {0:0, 1:1}
  def f(n: int) -> int:
    if n in memo:
      return memo[n]
    memo[n] = max(f(n//2) + f(n//3) + f(n//4) + f(n//5), n)
    return memo[n]
  return f(n)