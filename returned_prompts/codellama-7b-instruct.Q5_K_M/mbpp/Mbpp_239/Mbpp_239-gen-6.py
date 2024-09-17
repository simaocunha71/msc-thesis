
def get_total_number_of_sequences(m: int, n: int) -> int:
  current = 1
  total = 0
  for i in range(n):
    total += current
    current = current * 2
    if current > m:
      current = m
  return total


