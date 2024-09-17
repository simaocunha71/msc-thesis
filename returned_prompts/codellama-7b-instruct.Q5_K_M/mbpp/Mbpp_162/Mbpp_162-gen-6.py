
def sum_series(n: int) -> int:
  series_sum = 0
  for i in range(n // 2):
    series_sum += n - 2 * i
  return series_sum


