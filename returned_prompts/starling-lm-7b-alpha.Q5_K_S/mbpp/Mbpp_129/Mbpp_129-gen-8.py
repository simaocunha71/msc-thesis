
def magic_square_test(matrix):
  n = len(matrix)
  if n % 2 != 0 or len(matrix[0]) != n:
    return False
  sums = []
  for row in matrix:
    if not all(x % (n + 1) == 0 for x in row):
      return False
    if sum(row) % (n + 1):
      return False
    sums.append(sum(row))
  sums.sort()
  return all(sums[i] == sums[i + 1] + 1 for i in range(n))


