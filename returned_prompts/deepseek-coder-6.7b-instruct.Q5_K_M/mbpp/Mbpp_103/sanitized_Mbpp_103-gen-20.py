def eulerian_num(n: int, m: int) -> int:
  euler_arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
  for i in range(n+1):
    euler_arr[i][0] = 0
    euler_arr[i][i] = 1
  for i in range(2, n+1):
    for j in range(1, i):
      euler_arr[i][j] = euler_arr[i-1][j-1] + j*euler_arr[i-1][j]
  return euler_arr[n][m]