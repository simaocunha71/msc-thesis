
def count_binary_seq(n):
  count = [[0]*(2*n+1) for _ in range(n+1)]
  for i in range(2*n+1):
    count[0][i] = 1
  for i in range(1, n+1):
    for j in range(i, 2*n+1):
      count[i][j] = count[i-1][j-1] + count[i][j-1]
  return count[n][2*n]


