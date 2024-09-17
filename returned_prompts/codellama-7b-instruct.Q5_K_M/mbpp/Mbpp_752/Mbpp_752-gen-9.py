
def jacobsthal_num(n: int) -> int:
  def jacobsthal_num_helper(num: int, n: int) -> int:
    if n == 1:
      return num
    else:
      return jacobsthal_num_helper(num + (2**(n-1))*num, n-1)
  return jacobsthal_num_helper(1, n)
