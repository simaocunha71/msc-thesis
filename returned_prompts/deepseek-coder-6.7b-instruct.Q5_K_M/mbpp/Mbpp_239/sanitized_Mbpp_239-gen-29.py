def get_total_number_of_sequences(m: int, n: int) -> int:
  sequence = [[0 for _ in range(n+1)] for _ in range(m+1)] 
  for i in range(1, m+1):
    sequence[i][1] = 1
  for i in range(2, n+1):
    for j in range(1, m+1):
      for k in range(1, j):
        sequence[j][i] += sequence[k][i-1]
  total_count = 0
  for i in range(1, m+1):
    total_count += sequence[i][n]
  return total_count