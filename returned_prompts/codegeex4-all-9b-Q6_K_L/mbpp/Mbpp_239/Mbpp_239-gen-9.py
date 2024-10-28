def get_total_number_of_sequences(m: int, n: int) -> int:
  def helper(m: int, n: int, prev: int) -> int:
    if n == 0:
      return 1
    count = 0
    for i in range(prev*2, min(m, prev*2 + 1)):
      count += helper(m, n-1, i)
    return count
  return helper(m, n, 1)